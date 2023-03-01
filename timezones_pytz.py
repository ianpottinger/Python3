import pytz
from datetime import datetime

# Get a list of all available time zones
time_zones = pytz.all_timezones

# Loop through all time zones and print the current time in each
for zone in time_zones:
    # Get the timezone object for the current zone
    tz = pytz.timezone(zone)
    # Get the current time in the current timezone
    time = datetime.now(tz)
    # Print the current time in the current timezone
    print(f"{zone}: {time.strftime('%Y-%m-%d %H:%M:%S')}")
