from check_weather import CheckWeather, should_i_water
from relay_control import RelayControl
from log import Log


class RunParameters:
    def __init__(self, watering_time, watering_mode):
        self.watering_time = watering_time
        self.watering_mode = watering_mode

    def __iter__(self):
        for attr, value in vars(self):
            yield attr, value


if __name__ == '__main__':

#         run_mode = "running_on_pi"
#     except ModuleNotFoundError:
#         from fake_relay_control import RelayControl
#         run_mode = "running_on_pi"

    # Set up watering time (in seconds)
    run_params = RunParameters(
        watering_time=10,
        watering_mode="daily",
    )

    log = Log(run_params)

    # TODO define two watering modes: daily and when_necessary
    # TODO define a class WateringParameters & store to log
    # TODO switch watering mode to daily and store run_mode in log (depends on if RelayControl imports RPi)
    # check_weather = CheckWeather()

    # decision_to_water = should_i_water(check_weather.passed_rain())
    decision_to_water = False
    # date = check_weather.date(i)
    # precipitation = check_weather.daily_precipitation(i)

    log.add_watering_specification(decision_to_water=decision_to_water)

    if decision_to_water:
        RelayControl().activate(run_params.watering_time)

    print(log)
