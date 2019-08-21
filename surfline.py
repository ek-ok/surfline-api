import decimal
import json
import logging

import grequests
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.utils import urlparse


# Create logging
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def roundup(n):
    """In Python 3 round(0.5) is 0. This function returns 1"""
    return int(decimal.Decimal(n).quantize(decimal.Decimal('1'),
                                           rounding=decimal.ROUND_HALF_UP))


def parse_get_params(url):
    """Parses params from a GET URL"""
    params = dict(x.split('=') for x in urlparse(url).query.split('&'))
    return params['spotId']


def fetch_conditions(spot_ids, days):
    """Call Surfline API to request conditions"""
    url = "http://services.surfline.com/kbyg/spots/forecasts/conditions?spotId={}&days={}"

    # Define retry logic
    retries = Retry(total=5, status_forcelist=[500, 502, 503, 504])
    s = Session()
    s.mount('http://', HTTPAdapter(max_retries=retries))

    # Concurrently fetch Surfline API
    reqs = (grequests.get(url.format(_id, days), session=s) for _id in spot_ids)
    results = grequests.map(reqs)
    return {parse_get_params(r.request.url): json.loads(r.text)['data']['conditions'] for r in results}


def lambda_handler(event, context):
    """API endpoint"""
    logging.info('surfline-API started')

    spot_ids = event['multiValueQueryStringParameters']['spotId']
    days = event['queryStringParameters']['days']
    logging.info('%s spotIds and %s days are passed', len(spot_ids), days)

    conditions = fetch_conditions(spot_ids, days)
    logging.info('Fetched Surfline API')

    return {'statusCode': 200, 'body': json.dumps(conditions)}
