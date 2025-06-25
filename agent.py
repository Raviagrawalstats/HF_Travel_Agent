from smolagents import CodeAgent, Tool
from tools import get_weather_forecast, get_places
from itinerary import generate_itinerary

def main():
    print("Welcome to the Travel Itinerary Agent!")
    city = input("Which city or region do you want to visit? ")
    days = int(input("How many days do you want to stay? "))
    pref = input("What type of trip? (beach/mountain/city/historical): ")
    start_date = input("When do you want to start? (YYYY-MM-DD): ")

    # Define tools for the agent
    weather_tool = Tool(
        name="get_weather_forecast",
        func=get_weather_forecast,
        description="Get weather forecast for a city"
    )

    # Simple agent logic (can be expanded)
    weather = weather_tool(city, start_date, days)
    if not isinstance(weather, str):
        weather = str(weather)
    pref_map = {
        "beach": "tourist_attraction",
        "mountain": "park",
        "city": "museum",
        "historical": "museum"
    }
    place_type = pref_map.get(pref, "tourist_attraction")
    places_per_day = 3
    places = get_places(city, place_type, days * places_per_day)
    itinerary = generate_itinerary(city, days, weather, pref, places)

    print("\nYour personalized itinerary:\n")
    print(itinerary)

if __name__ == "__main__":
    main()