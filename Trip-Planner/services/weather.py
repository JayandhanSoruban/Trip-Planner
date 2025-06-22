# trip_planner/services/weather.py

import os
from pyowm import OWM
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

API_KEY = os.getenv("OWM_API_KEY")
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city_name):
    observation = mgr.weather_at_place(city_name)
    weather = observation.weather
    status = weather.detailed_status
    temperature = weather.temperature('celsius')["temp"]
    return {
        "city": city_name,
        "status": status,
        "temperature": temperature
    }