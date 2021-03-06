import json
import requests
from instance.config import AppConfig

def get_location_coordinates(location_name):
    """
    Function that gets the location coordinates of
    specific location
    Args:
        location_name (str): the selected location
    Return:
        location_data (dict): the location data
    """

    google_api_key = AppConfig.GOOGLE_API_KEY
    url = AppConfig.GCP_URL.format(
            location_name, google_api_key)

    res = json.loads(requests.get(url).content)


    latitude = res['results'][0]['geometry']['location']['lat']
    longitude = res['results'][0]['geometry']['location']['lng']
    city = res['results'][0]['formatted_address']
    location = "{}, {}".format(latitude, longitude)


    location_data = {
        "latitude": latitude,
        "longitude": longitude,
        "city": city,
        "location": location
    }


    return location_data
