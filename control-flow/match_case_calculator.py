from datetime import datetime
import pytz

def show_time(city):
    # Dictionary of city to timezone mapping
    timezones = {
        "houston": "America/Chicago",
        "new york": "America/New_York",
        "london": "Europe/London",
        "lagos": "Africa/Lagos",
        "nairobi": "Africa/Nairobi",
        "tokyo": "Asia/Tokyo",
        "dubai": "Asia/Dubai"
    }

    city = city.lower()

    if city in timezones:
        tz = pytz.timezone(timezones[city])
        city_time = datetime.now(tz)
        print(f"The time in {city.title()} is {city_time.strftime('%I:%M:%S %p on %A, %B %d, %Y')}")
    else:
        print("Sorry, that city is not in our list.")

# Ask user for input
user_city = input("Enter a city (e.g., Houston, London, Lagos): ")
show_time(user_city)
