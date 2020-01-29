## Weather App
#### This is a simple weather application. It displays the prevailing weather condition of location

### Requirements
 - [Python](https://www.python.org/)
 - [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
 - [Google cloud platform](https://console.cloud.google.com/apis/credentials)
 - - Create a google app to get an Api key that will help you use the Google Geocoding feature
 - [Dark Sky Api](https://darksky.net)
 - - Dark sky api, help you to get the prevailing weather condition of a specific area


### Setup the app locally
- `git clone https://github.com/Georgeygigz/weather-app`
- cd `weather-app`
- run `pipenv shell` to activate the virtual environment
- run `pipenv install` to install dependencies
- create .env and place in the following environmental variables

    ```
        DARK_SKY_SECRET_KEY=<your_dark_sky_secret_key>
        GOOGLE_API_KEY=<your_google_api_key>
    ```
- Get your DARK_SKY_SECRET_KEY and GOOGLE_API_KEY and replace them in the .env file
- You can get the GOOGLE API KEY in the [google console](https://console.cloud.google.com/apis/credentials) by creating project in the google console, and then create credentials to get the api key
- Sign up to [dark sky](https://darksky.net/dev) and Navigate to the dashbord to get your Dark sky secret key
- run `source .env` to export environment variables
- run `python run.py` to start the server
- navigate to `http://127.0.0.1:5000/`

## Running tests
- use this command to run test and the coverage report
- `nosetests --with-coverage --cover-package=app && coverage report`