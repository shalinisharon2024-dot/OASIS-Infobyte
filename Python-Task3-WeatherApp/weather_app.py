"""
Oasis Infobyte Python Programming Internship
Task: Basic Weather App
Description: Fetches real-time weather metrics for any city globally 
using the OpenWeatherMap API and the Python requests library.
"""

import requests

def get_weather():
    print("=" * 45)
    print("       REAL-TIME BASIC WEATHER APP      ")
    print("=" * 45)
    
    # Free demo API key or your own key from openweathermap.org
    api_key = "2e6f234383431666e6c51480f2d48651" 
    city = input("Enter city name (e.g., Hyderabad, London, New York): ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=387124f8754b2556a0d3a481ad0dccdb&units=metric"

    print(f"\n🔍 Fetching weather data for {city.title()}...")

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            weather_desc = data['weather'][0]['description'].capitalize()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            country = data['sys']['country']

            print("\n" + "=" * 45)
            print(f"🌤️ WEATHER REPORT: {city.title()}, {country}")
            print("=" * 45)
            print(f"   • Condition   : {weather_desc}")
            print(f"   • Temperature : {temp}°C (Feels like {feels_like}°C)")
            print(f"   • Humidity    : {humidity}%")
            print(f"   • Wind Speed  : {wind_speed} m/s")
            print("=" * 45)
        else:
            error_message = data.get('message', 'Unknown error')
            print(f"\n❌ Error: Could not retrieve weather data. Reason: {error_message.capitalize()}")

    except requests.exceptions.Timeout:
        print("\n❌ Error: Request timed out. Please check your internet connection.")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ A network error occurred: {e}")

if __name__ == "__main__":
    get_weather()
