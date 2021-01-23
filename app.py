from src.api.rides import RidesResource
from src.api.calculation import CalculationResource
from falcon_cors import CORS
import falcon


cors = CORS(
    allow_origins_list=['*'],
    allow_all_origins=True,
    allow_all_headers=True,
    allow_all_methods=True
)


api = falcon.API(middleware=[cors.middleware])

api.add_route('/v1/rides', RidesResource())
api.add_route('/v1/calculation', CalculationResource())