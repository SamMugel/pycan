from check_weather import CheckWeather, should_i_water
from relay_control import RelayControl


if __name__ == '__main__':
    # Set up watering time (in seconds)
    watering_time = 10
    check_weather = CheckWeather()

    if should_i_water(check_weather.passed_rain()):
        RelayControl().activate(watering_time)
