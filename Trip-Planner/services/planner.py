# trip_planner/services/planner.py

import os
from dotenv import load_dotenv
from services.location import LocationService
from services.weather import get_weather
import requests

load_dotenv()

class TripPlanner:
    def __init__(self, location_data):
        self.location_data = location_data
        self.lat = location_data["latitude"]
        self.lon = location_data["longitude"]
        self.city = location_data["input"]
        self.radius = 5000  # in meters

    def get_weather_info(self):
        return get_weather(self.city)

    def get_mock_attractions(self):
        # Replace with real data source if needed
        return [
            "City Park",
            "Historical Museum",
            "Art Gallery",
            "Riverfront Walk"
        ]

    def get_mock_activities(self):
        return [
            "Sunset photography",
            "City heritage walk",
            "Museum tours",
            "Local food exploration"
        ]

    def get_restaurants(self):
        api_key = os.getenv("GEOAPIFY_API_KEY")
        if not api_key:
            print("❌ Geoapify API key missing.")
            return []

        url = "https://api.geoapify.com/v2/places"
        params = {
            "categories": "catering.restaurant",
            "filter": f"circle:{self.lon},{self.lat},{self.radius}",
            "limit": 5,
            "apiKey": api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            return [
                place['properties'].get('name', 'Unnamed Restaurant')
                for place in data.get('features', [])
            ]
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch restaurants: {e}")
            return []

    def get_transport_options(self):
        return [
            {"type": "Metro", "availability": "High", "average_cost_per_day": 100},
            {"type": "Auto Rickshaw", "availability": "Medium", "average_cost_per_day": 300},
            {"type": "Cab (Ola/Uber)", "availability": "High", "average_cost_per_day": 600},
        ]

    def generate_plan(self):
        print(f"\n📍 Location: {self.city}")

        weather = self.get_weather_info()
        print(f"\n🌤️ Weather in {weather['city']}: {weather['status'].capitalize()}, {weather['temperature']}°C")

        attractions = self.get_mock_attractions()
        print(f"\n📌 Top Attractions: {attractions}")

        activities = self.get_mock_activities()
        print(f"\n🎯 Activities: {activities}")

        restaurants = self.get_restaurants()
        print(f"\n🍴 Restaurants Nearby: {restaurants if restaurants else 'No results found'}")

        transport = self.get_transport_options()
        print(f"\n🚗 Transport Options: {transport}")


if __name__ == "__main__":
    loc_service = LocationService()
    user_location = loc_service.request_location_from_user()

    if user_location:
        planner = TripPlanner(user_location)
        planner.generate_plan()
