from datetime import datetime
from urllib.parse import quote

# Function to create Google Calendar event URL
def create_google_calendar_url(title, date, start_time, end_time, description, location):
    # Convert date and time to datetime objects
    date_format = "%d/%m/%Y"
    time_format = "%H:%M"
    datetime_start = datetime.strptime(f"{date} {start_time}", f"{date_format} {time_format}")
    datetime_end = datetime.strptime(f"{date} {end_time}", f"{date_format} {time_format}")

    # Convert datetime objects to Google Calendar format
    google_calendar_format = "%Y%m%dT%H%M%SZ"
    start_utc = datetime_start.strftime(google_calendar_format)
    end_utc = datetime_end.strftime(google_calendar_format)

    # Encode text for URL compatibility
    title_encoded = quote(title)
    description_encoded = quote(description)
    location_encoded = quote(location)

    # Create URL
    url = f"https://calendar.google.com/calendar/u/0/r/eventedit?text={title_encoded}&dates={start_utc}/{end_utc}&details={description_encoded}&location={location_encoded}"

    return url

# Event details section
title = "TITLE"
date = "03/04/2024" # (DD/MM/YYYY)
start_time = "14:00" # (UTC, HH:MM, 24-hour format)
end_time = "14:45" # (UTC, HH:MM, 24-hour format)
description = """DESCRIPTION"""
location = "LOCATION"

# Generate the URL
event_url = create_google_calendar_url(title, date, start_time, end_time, description, location)
print("Your Google Calendar event URL is:")
print(event_url)
