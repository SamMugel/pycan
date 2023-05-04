import pyowm


class CheckWeather:
    pyown_api_key = 'd1474d4367c8c2cfb7bd6ba566f34f94'

    def __init__(self, location: str = 'Toronto,CA'):
        self.location = location
        self.weather = self.get_weather()

    def get_weather(self):
        # Set up OpenWeatherMap API key
        owm = pyowm.OWM(self.pyown_api_key)
        manager = owm.weather_manager()
        observation = manager.weather_at_place(self.location)
        return observation.weather

    def is_it_raining(self):
        # Check if it's raining
        is_raining = self.weather.get_rain().get('1h', 0) > 0
        return is_raining


if __name__ == '__main__':
    check_weather = CheckWeather()
    check_weather.is_it_raining()