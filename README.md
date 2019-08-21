# Surfline API

`Surfline API` returns wave forecasts for a given spots and number of days by concurrently fetcheing Surfline's **Know Before You Go** service. It is implemented on AWS Lambda. `function.zip` was built using EC2 `ami-035b3c7efe6d061d5` image.

Add `surfline.py` to `function.zip` by running the below command and upload `function.zip` to Lambda.
```
zip -g function.zip surfline.py
```

## API Interface
You can pass multiple `spotId`s and `days`. `spotId` is Surfline's spot identifiler.

For example,
`https://y36qk3xd7h.execute-api.us-east-1.amazonaws.com/default/surfline-api?spotId=5842041f4e65fad6a7708a21&spotId=5842041f4e65fad6a7708a20&days=6`


