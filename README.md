# ride-app-api
API
| Endpoint | Description |
| ----------- | ----------- |
| /v1/rides | Get list of rides |
| /v1/calculation?id={id_ride} | Calculate price of ride identified by id | 

## Install requirements.txt
pip install -r requirements.tx

## Start server
gunicorn app:api