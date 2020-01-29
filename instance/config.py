# instance/config.py
import os
import sys
class Config():
    DEBUG=False
    DARK_SKY_SECRET_KEY=os.getenv("DARK_SKY_SECRET_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GCP_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
    DARK_SKY_BASE_URL = "https://api.darksky.net/forecast"


class DevelopmentConfig(Config):
    """
    Enable our debug mode to True
    in development in order to auto
    restart our server on code changes
    """
    DEBUG = True

app_configuration={
    'development': DevelopmentConfig
}

AppConfig = app_configuration.get('development')