import requests
import json
import time
from .location_coordinates import get_location_coordinates
from instance.config import AppConfig

def get_weather_data(location_name):
    """
    Function to get the weather data
    Args:
        location_name (str): location_name
    Returns:
    """

    dark_sky_base_url = AppConfig.DARK_SKY_BASE_URL
    dark_sky_secret_key = AppConfig.DARK_SKY_SECRET_KEY


    location_data = get_location_coordinates(location_name)
    location = location_data['location']
    city = location_data['city']


    dark_sky_url = "{}/{}/{}".format(
        dark_sky_base_url,dark_sky_secret_key,location)

    response = json.loads(requests.get(dark_sky_url).content)
    response.update({"city":city})

    return response
