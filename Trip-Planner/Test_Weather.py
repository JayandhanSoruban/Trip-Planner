# test_weather.py
from services.weather import get_weather


def test():
    city = "Chennai"  # You can test with any city
    weather_info = get_weather(city)
    print(f"Weather in {city}:")
    print(f"Status: {weather_info['status']}")
    print(f"Temperature: {weather_info['temperature']}°C")

if __name__ == "__main__":
    test()
