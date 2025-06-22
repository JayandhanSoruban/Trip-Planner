from services.weather import get_weather
from services.currency import convert_currency
from services.itinerary import create_itinerary
from services.summary import print_summary

def plan_trip():
    city = input("Enter your destination city: ")
    date = input("Enter your travel date (YYYY-MM-DD): ")
    budget = float(input("Enter your budget in INR: "))

    weather = get_weather(city)
    budget_usd = convert_currency(budget, "INR", "USD")
    itinerary = create_itinerary(city, date)
    
    print_summary(city, date, weather, budget_usd, itinerary)
