# location.py

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError


class LocationService:
    def __init__(self, user_agent="trip_planner_agent"):
        self.geolocator = Nominatim(user_agent=user_agent)

    def request_location_from_user(self):
        """Prompt user to input their location and return structured info."""
        user_input = input("🔍 Please enter your location (e.g., city, landmark, or full address): ").strip()
        if not user_input:
            print("⚠️ Location input cannot be empty.")
            return None

        return self.get_location_info(user_input)

    def get_location_info(self, place_name):
        """Convert location string to structured data."""
        try:
            location = self.geolocator.geocode(place_name)
            if location:
                return {
                    "input": place_name,
                    "address": location.address,
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                }
            else:
                print(f"❌ Could not find the location: {place_name}")
                return None
        except GeocoderServiceError as e:
            print(f"⚠️ Geocoding error: {e}")
            return None


# Example usage
if __name__ == "__main__":
    loc_service = LocationService()
    result = loc_service.request_location_from_user()
    if result:
        print("\n📍 Location Details:")
        print(f"Address   : {result['address']}")
        print(f"Latitude  : {result['latitude']}")
        print(f"Longitude : {result['longitude']}")
