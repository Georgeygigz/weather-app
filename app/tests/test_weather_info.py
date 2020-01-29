import unittest
from unittest.mock import patch,Mock
import json
from app.views import app


class WeatherInfoTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.weather_data ={
            "currently":{"time":1580260089, "summary":"Mostly Cloudy",
                        "temperature":60.28, "humidity":0.97, "windSpeed": 3.72,
                        "cloudCover":0.85, "visibility":10, "pressure":1013.8},
            "hourly": {"summary":
            "Possible light rain starting this evening, continuing until tomorrow morning."},
            "daily": {"summary": "Rain throughout the week." },
            "timezone": "Africa/Nairobi"
        }

        self.location_data ={
            "results": [{"geometry":{
            "location": {"lat": -1.2920659, "lng": 36.8219462}},
            "formatted_address":'Nairobi, Kenya'}]}


    @patch("requests.get")
    def test_get_weather_info_succeeds(self, mock_obj):
        mock_responses = [Mock(), Mock()]
        mock_responses[0].content = json.dumps(self.location_data).encode()
        mock_responses[1].content= json.dumps(self.weather_data).encode()
        mock_obj.side_effect = mock_responses

        res = self.app.get('location/Nairobi')
        response = json.loads(res.data)['data']


        self.assertEqual(
            response['city'],
            self.location_data['results'][0]['formatted_address'])
        self.assertEqual(
            response['current_summary'],
            self.weather_data['currently']['summary'])


    @patch("app.views.render_template")
    def test_land_home_page_succeeds(self, mock_render_template):
        res = self.app.get('/')

        mock_render_template.return_value=True
        self.assertTrue(mock_render_template.called)


