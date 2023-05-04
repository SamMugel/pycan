import pyowm
from pyowm.utils import timestamps, formatting


class CheckWeather:
    pyown_api_key = 'd1474d4367c8c2cfb7bd6ba566f34f94'

    def __init__(self, location: str = 'Toronto,CA'):
        self.location = location
        self.owm = pyowm.OWM(self.pyown_api_key)
        self.manager = self.owm.weather_manager()

    def forecast_rainfall(self, interval: str = '3h'):
        forecast = self.manager.forecast_at_place(self.location, interval)
        weather = forecast.get_weather_at('2023-05-04 18:00:00+00:00')
        return weather.rain

    # fc = owm.daily_forecast('Oklahoma City,US', 8)
    # tomorrow = fc.get_weather_at('2017-04-04 18:00:00+00')
    # print(tomorrow.get_rain())
    # # {'all': 1.73}
    # print(tomorrow.get_detailed_status())

    # light rain

    def current_rainfall(self, interval: str = '3h'):
        observation = self.manager.weather_at_place(self.location)
        weather = observation.weather
        rainfall = weather.rain
        return rainfall

    def daily_forecast(self):
        one_call = self.manager.one_call(*self.get_coords())
        return one_call.forecast_daily

    def hourly_history(self):
        yesterday_epoch = formatting.to_UNIXtime(timestamps.yesterday())
        print(self.get_coords())
        one_call = self.manager.one_call_history(*self.get_coords(), yesterday_epoch)
        return one_call.forecast_hourly

    def get_coords(self):
        mgr = self.owm.geocoding_manager()
        # geocode London (no country specified) - we'll get many results
        list_of_locations = mgr.geocode(self.location)
        location = list_of_locations[0]  # taking the first London in the list
        return location.lat, location.lon


if __name__ == '__main__':
    check_weather = CheckWeather()
    print('current rainfall is: %s' % check_weather.current_rainfall())
    print('future rainfall is: %s' % check_weather.forecast_rainfall())

    print('forecast')
    for forecast in check_weather.daily_forecast():
        print(forecast.rain)

    print('historical')
    for forecast in check_weather.hourly_history():
        print(forecast.rain)




