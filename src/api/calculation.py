import falcon
import json
from src.data.data import DATA_RIDES
from src.helper.util import ( 
                            get_ride_price,
                            get_ride_by_id
                            )



class CalculationResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        result = dict()
        ride_id = req.get_param_as_int('id')
        ride = get_ride_by_id(ride_id)
        price = get_ride_price(ride)
        result['id'] = ride_id
        result['price'] = price
        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200
