from datetime import date
from check_weather import CheckWeather, should_i_water
from relay_control import RelayControl


def log(decision_to_water: bool):
    log = "Today's date, {0}\n".format(date.today())
    log += "decision to water: {0}\n\n".format(decision_to_water)
    for i in range(2):
        log += "day index, {0}\n".format(i)
        log += "date, {0}\n".format(check_weather.date(i))
        log += "precipitation, {0}mm\n\n".format(check_weather.daily_precipitation(i))

    return log


if __name__ == '__main__':
    # Set up watering time (in seconds)
    watering_time = 10
    check_weather = CheckWeather()

    decision_to_water = should_i_water(check_weather.passed_rain())
    if decision_to_water:
        RelayControl().activate(watering_time)
        
    print(log(decision_to_water))
