def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) / 1.8
  return celsius

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 1.8) + 32
  return fahrenheit

fah = float(98.6)
cel = fahrenheit_to_celsius(fah)

print('Fahrenheit = ', fah)
print('Celsius = ', cel)

cel = 37
fah = celsius_to_fahrenheit(cel)

print('Celsius = ', cel)
print('Fahrenheit = ', fah)
