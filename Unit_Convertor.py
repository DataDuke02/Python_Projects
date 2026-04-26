def convert_length(value, from_unit, to_unit):
    length_units = {'M1': 1, 'KM': 1000, 'M2' : 1609.34, 'F': 0.3048}
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Unsupported length unit.")
    return value * length_units[from_unit]/length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {'G': 1, 'KG': 1000, 'P' : 453.592}
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Unsupported weight unit.")
    return value * weight_units[from_unit]/weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
    raise ValueError("Unsupported temperature unit.")

def main():
    print("Unit Convertor")
    print(" 1 : Length")
    print(" 2 : Weight")
    print(" 3 : Temperature")

    choice = input("Choose the type of conversion (1/2/3) : ")

    if choice == '1':
        value = float(input("Enter value : "))
        from_unit = input("from unit ( M1 - meters, KM - kilometers, M2 - miles, F - feet) : ").upper()
        to_unit = input("To unit (M1 - meters, KM - kilometers, M2 - miles, F - feet) : ").upper()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '2':
        value = float(input("Enter value : "))
        from_unit = input("from unit (G - grams, KG - kilograms,  P - pounds) : ").upper()
        to_unit = input("To unit (G - grams, KG - kilograms, P - pounds) : ").upper()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    if choice == '3':
        value = float(input("Enter value : "))
        from_unit = input("from unit (C - celsius, F - fahrenheit, K - kelvin) : ").upper()
        to_unit = input("To unit (C - celsius, F - fahrenheit, K - kelvin) : ").upper()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    else:
        print("Invalid Choices")

if __name__ == "__main__":
    main()
