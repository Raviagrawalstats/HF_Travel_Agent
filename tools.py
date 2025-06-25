import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHERAPI_KEY")


def get_weather_forecast(city, start_date, days):
    """
    Fetches weather forecast for a city for the given dates.
    """
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}&aqi=no&alerts=no"
    resp = requests.get(url)
    if resp.status_code != 200:
        return ""
    data = resp.json()
    # Simplified: just return the first 'days' forecasts
    forecasts = []
    for entry in data["forecast"]["forecastday"]:
        date = entry["date"]
        temp = entry["day"]["avgtemp_c"]
        desc = entry["day"]["condition"]["text"]
        forecasts.append(f"{date}: {temp}°C, {desc}")
        if len(forecasts) >= days:
            break
    return "\n".join(forecasts)


def get_places(city, category, limit=10):
    api_key = os.getenv("GOOGLE_PLACES_API_KEY")
    geo_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={api_key}"
    geo_resp = requests.get(geo_url)
    print("Geocode response:", geo_resp.json())  # Debug print
    if geo_resp.status_code != 200 or not geo_resp.json().get("results"):
        return []
    location = geo_resp.json()["results"][0]["geometry"]["location"]
    lat, lng = location["lat"], location["lng"]

    search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": 5000,
        "type": category,
        "key": api_key
    }
    resp = requests.get(search_url, params=params)
    print("Places response:", resp.json())  # Debug print
    if resp.status_code != 200:
        return []
    data = resp.json()
    return [place["name"] for place in data.get("results", [])[:limit]]