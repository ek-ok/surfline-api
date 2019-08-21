# Surfline API

`Surfline API` returns wave forecasts for a given spots and number of days by concurrently fetcheing Surfline's **Know Before You Go** service. It is implemented on AWS Lambda. `function.zip` contains all the packages in `requirements.txt` for Python 3.7. It was built using EC2 `ami-035b3c7efe6d061d5` image for a compatibility reason.

Add `surfline.py` to `function.zip` by running the below command and upload `function.zip` to Lambda.
```
zip -g function.zip surfline.py
```

## API Interface
You can pass multiple `spotId`s and `days`. `spotId` is Surfline's spot identifiler.

For example,

`https://y36qk3xd7h.execute-api.us-east-1.amazonaws.com/default/surfline-api?spotId=5842041f4e65fad6a7708a21&spotId=5842041f4e65fad6a7708a20&days=6`

### Other Surfline's Know Before You Go services

KBYG Subregional Overview

`http://services.surfline.com/kbyg/regions/overview?subregionId=58581a836630e24c4487900b`


KBYG Subregional Forecasts:
`http://services.surfline.com/kbyg/regions/forecasts?subregionId=58581a836630e24c4487900b`

KBYG Regional Analyses:
`http://services.surfline.com/feed/regional?subregionId=58581a836630e24c4487900b`

KBYG Mapview Spots:
`http://services.surfline.com/kbyg/mapview?south=33.667782574792184&west=-118.56994628906251&north=34.028762179464465&east=-118.04054260253908`

KBYG Conditions:
`http://services.surfline.com/kbyg/spots/forecasts/conditions?spotId=5842041f4e65fad6a7708906&days=6`

KBYG Tides:
`http://services.surfline.com/kbyg/spots/forecasts/tides?spotId=5842041f4e65fad6a7708906&days=1`

KBYG Waves:
`http://services.surfline.com/kbyg/spots/forecasts/wave?spotId=5842041f4e65fad6a7708906&days=1&intervalHours=1`

KBYG Weather:
`http://services.surfline.com/kbyg/spots/forecasts/weather?spotId=5842041f4e65fad6a7708906&days=1&intervalHours=1`

KBYG Wind:
`http://services.surfline.com/kbyg/spots/forecasts/wind?spotId=5842041f4e65fad6a7708906&days=1&intervalHours=1`
