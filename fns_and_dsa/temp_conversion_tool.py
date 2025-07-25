FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    try:
        temp = int(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        break
    scale = (input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()

    match scale:
        case "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        case "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        case _:
            print("Invalid temperature unit.")
    break
