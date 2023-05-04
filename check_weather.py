import pyowm
from pyowm.utils import timestamps, formatting


def read_precipitation(rain: dict):
    try:
        return rain['all']
    except KeyError:
        return 0


class CheckWeather:
    pyown_api_key = 'd1474d4367c8c2cfb7bd6ba566f34f94'

    def __init__(self, location: str = 'Toronto,CA'):
        self.location = location
        self.owm = pyowm.OWM(self.pyown_api_key)
        self.manager = self.owm.weather_manager()

    def daily_precipitation(self, day_index: int = 0):
        one_call = self.manager.one_call(*self.get_coords())
        daily_forecast = one_call.forecast_daily
        precipitation = daily_forecast[day_index].rain
        return read_precipitation(precipitation)

    def get_coords(self):
        mgr = self.owm.geocoding_manager()
        # geocode London (no country specified) - we'll get many results
        list_of_locations = mgr.geocode(self.location)
        location = list_of_locations[0]  # taking the first London in the list
        return location.lat, location.lon


if __name__ == '__main__':
    check_weather = CheckWeather()
    print("today's forecast precipitation is: %s mm" % check_weather.daily_precipitation())
    print("tomorrow's forecast precipitation is: %s mm" % check_weather.daily_precipitation(1))



