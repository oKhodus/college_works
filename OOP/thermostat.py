class Thermostat:
    def __init__(self, temp_c):
        self._temp_c = None
        self.temp_c = temp_c

    @property
    def temp_c(self):
        return self._temp_c

    @temp_c.setter
    def temp_c(self, value):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                raise ValueError("Temperature must be a number.")
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature must be a number.")

        if value < -50 or value > 150:
            raise ValueError("Temperature must be between -50 and 150 °C.")

        self._temp_c = float(value)

    def to_fahrenheit(self):
        return (self._temp_c * 9/5) + 32
        

t = Thermostat(20.0)
print(t.temp_c)
t.temp_c = 25.0
print(t.temp_c)
print(round(t.to_fahrenheit(), 1))