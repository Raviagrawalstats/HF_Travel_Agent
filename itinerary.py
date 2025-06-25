# def generate_itinerary(city, days, weather_forecast, preferences):
#     """
#     Generates a simple itinerary based on city, days, weather, and preferences.
#     """
#     activities = {
#         "beach": ["Relax at the beach", "Try water sports", "Enjoy seaside dining"],
#         "mountain": ["Go hiking", "Visit scenic viewpoints", "Try local cuisine"],
#         "city": ["Visit museums", "Explore historic sites", "Enjoy local cafes"],
#         "historical": ["Tour ancient landmarks", "Visit museums", "Walk old town"]
#     }
#     chosen_activities = activities.get(preferences, activities["city"])
#     itinerary = []
#     weather_lines = weather_forecast.split("\n")
#     for i in range(days):
#         day = f"Day {i+1}: {chosen_activities[i % len(chosen_activities)]} ({weather_lines[i] if i < len(weather_lines) else ''})"
#         itinerary.append(day)
#     return "\n".join(itinerary)

def generate_itinerary(city, days, weather_forecast, preferences, places):
    """
    Generates a detailed itinerary using real places.
    """
    itinerary = []
    weather_lines = weather_forecast.split("\n")
    # Group places into chunks (e.g., 3 per day)
    places_per_day = 3
    for i in range(days):
        start = i * places_per_day
        day_places = places[start:start+places_per_day]
        places_str = ", ".join(day_places) if day_places else "No places found"
        weather_str = f" ({weather_lines[i]})" if i < len(weather_lines) and weather_lines[i] else ""
        day = f"Day {i+1}: {places_str}{weather_str}"
        itinerary.append(day)
    return "\n".join(itinerary)

