from datetime import date


class Log:
    def __init__(self, run_params):
        self.run_params = run_params
        self.content = ""
        self.add(f"Today's date: {date.today()}")
        self.add(f"Watering parameters: {str(vars(run_params))}")

    def add(self, line):
        self.content += line + "\n"

    def add_watering_specification(self, decision_to_water=True, check_weather=None):
        watering_mode = self.run_params.watering_mode
        if watering_mode != "daily" and check_weather is None:
            raise ValueError(f"Specify check_weather to use watering_mode: {watering_mode}")

        specification = self.watering_specification(decision_to_water, check_weather)
        self.add(specification)

    def watering_specification(self, decision_to_water, check_weather):
        specification = f"decision to water: {decision_to_water}\n"

        if check_weather is not None:
            for i in range(2):
                specification += f"day index, {i}\n"
                specification += f"date, {check_weather.date(i)}\n"
                specification += f"precipitation, {check_weather.daily_precipitation(i)}mm\n"

        return specification

    def __repr__(self):
        return self.content