def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_kelvin (celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_celsius (kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_kelvin (fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_fahrenheit(kelvin):
    fahrenheit = 1.8 * (kelvin - 273) + 32
    return fahrenheit

