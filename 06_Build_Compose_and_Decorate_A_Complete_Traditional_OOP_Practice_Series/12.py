# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
  @staticmethod 
  def celsius_to_fahrenheit(c):
    # formula: (C × 9/5) + 32 = F
    return (c * 9/5) + 32


temp_c = 37
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)  

print(f"{temp_c}°C = {temp_f}°F")