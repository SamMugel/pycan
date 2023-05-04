import time


def water_plants(watering_time: int):
    # Get current weather for your location

    # If it's not raining, water the plants
    if not is_raining:
        print("Watering the plants!")
        # TODO: Add code here to actually water the plants
        time.sleep(watering_time)


if __name__ == '__main__':
    # Set up watering time (in seconds)
    watering_time = 10
    while True:
        water_plants(watering_time)
        # Wait for some time before checking the weather again
        time.sleep(60)
