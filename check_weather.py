import pyowm
from datetime import datetime


def read_precipitation(rain: dict):
    try:
        return rain['all']
    except KeyError:
        return 0


def convert_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


class CheckWeather:
    pyown_api_key = 'd1474d4367c8c2cfb7bd6ba566f34f94'

    def __init__(self, location: str = 'Toronto,CA'):
        self.location = location
        self.owm = pyowm.OWM(self.pyown_api_key)
        self.daily_forecast = self.get_daily_forecast()

    def get_coords(self) -> tuple:
        mgr = self.owm.geocoding_manager()
        # geocode London (no country specified) - we'll get many results
        list_of_locations = mgr.geocode(self.location)
        location = list_of_locations[0]  # taking the first London in the list
        return location.lat, location.lon

    def get_daily_forecast(self):
        manager = self.owm.weather_manager()
        one_call = manager.one_call(*self.get_coords())
        return one_call.forecast_daily

    def date(self, day_index: int = 0) -> str:
        date = self.daily_forecast[day_index].ref_time
        return convert_timestamp(date)

    def daily_precipitation(self, day_index: int = 0) -> float:
        precipitation = self.daily_forecast[day_index].rain
        return read_precipitation(precipitation)

    def daily_weather(self, day_index: int = 0):
        weather = self.daily_forecast[day_index].status
        return weather

    def passed_rain(self) -> float:
        return self.daily_precipitation(0)

    def future_rain(self) -> float:
        return self.daily_precipitation(1)


# def should_i_water(passed_rain: float, future_rain: float, rain_threshold: float = None):
def should_i_water(passed_rain: float) -> bool:
    if passed_rain == 0:
        water = True
    else:
        water = False

    return water


if __name__ == '__main__':
    check_weather = CheckWeather()

    for i in range(7):
        print("the date in {0} days is {1}".format(i, check_weather.date(i)))
        print("the precipitation in {0} days is {1}mm".format(i, check_weather.daily_precipitation(i)))
        print("the weather in {0} days is {1}".format(i, check_weather.daily_weather(i)))

    print("decision to water: %s" % should_i_water(check_weather.passed_rain()))


