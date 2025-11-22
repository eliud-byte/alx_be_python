FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp = float(temp_str)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return 1

    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if scale == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.2f}°F")
    elif scale == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result:.2f}°C")
    else:
        print("Unknown scale. Please enter 'C' or 'F'.")
        return 1

    return 0

if __name__ == "__main__":
    main()


