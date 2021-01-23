import falcon
import json
from src.data.data import DATA_RIDES


class RidesResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.body = json.dumps(DATA_RIDES)
        resp.status = falcon.HTTP_200