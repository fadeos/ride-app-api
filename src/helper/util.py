
from datetime import datetime

from src.data.data import DATA_RIDES
from src.helper.const import (
    DATE_FORMAT,
    initial_charge,
    interval,
    price_per_mile
)



def check_period_eight_six(date_ride):
    hour = datetime.strptime(date_ride['startTime'], DATE_FORMAT)
    return True if hour >= 20 or hour <= 6 else False


def check_period_four_seven(date_ride):
    hour = datetime.strptime(date_ride['startTime'], DATE_FORMAT)
    return True if hour >= 16 or hour <= 19 else False


def get_ride_price(ride):
    price = 0
    price = initial_charge + (float(ride['distance']) / interval) * price_per_mile
    if check_period_eight_six:
        price += 0.5
    if check_period_four_seven:
        price += 1
    return price


def get_ride_by_id(ride_id):
    return [ride for ride in DATA_RIDES if ride['id'] == ride_id][0]
