import requests
import time
import os
import json
from flask import Flask, render_template, request
from .helpers.weather_data import get_weather_data
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/location/<location_name>', methods=['GET'])
@cross_origin()
def hello_world(location_name):

    response = get_weather_data(request.view_args['location_name'])

    current_time = response['currently']['time']
    formatted_time = time.strftime("%A %D %H:%M",
            time.localtime(int(current_time)))

    # weather data
    weather_data = {
    "current_summary": response['currently']['summary'],
    "current_time": current_time,
    "city": response['city'],
    "formatted_time": formatted_time,
    "temperature": response['currently']['temperature'],
    "humidity": response['currently']['humidity'],
    "wind_speed": response['currently']['windSpeed'],
    "cloud_cover": response['currently']['cloudCover'],
    "visibility": response['currently']['visibility'],
    "pressure": response['currently']['pressure'],
    "hourly_summary": response['hourly']['summary'],
    "daily_summary": response['daily']['summary']
    }

    return {"data": weather_data}