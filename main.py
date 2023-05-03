import pyowm
import time


# Define function to check the weather and water the plants if necessary
def check_weather_and_water_plants():
    # Get current weather for your location
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    # Check if it's raining
    is_raining = w.get_rain().get('1h', 0) > 0
    # If it's not raining, water the plants
    if not is_raining:
        print("Watering the plants!")
        # TODO: Add code here to actually water the plants
        time.sleep(watering_time)

# Main loop


if __name__ == '__main__':
    pyown_api_key = 'd1474d4367c8c2cfb7bd6ba566f34f94'
    location = '[43.7001, -79.4163]'

    # Set up OpenWeatherMap API key
    owm = pyowm.OWM(pyown_api_key)
    # Set up watering time (in seconds)
    watering_time = 10

    while True:
        check_weather_and_water_plants()
        # Wait for some time before checking the weather again
        time.sleep(60)
