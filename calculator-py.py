import math

while True:
    print("\n Choose the math Operations. \n\n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n 5 - Modulo \n 6 - Raising to a power \n 7 - Square root \n 8 - Logarithm  \n 9 - Sine \n 10 - Cosine \n 11 - Tangent")
    select = input("\n Your option from the menu: ")

    if select in ["1", "2", "3", "4"]:
        num_values = input("\n How many values do you want to " + ("add" if select == "1" else "subtract" if select == "2" else "multiply" if select == "3" else "divide") + "? ")

        try:
            num_values = int(num_values)
            values = []

            for i in range(num_values):
                value = float(input("\n Enter value #" + str(i + 1) + ": "))
                values.append(value)

            if select == "1":
                result = sum(values)
            elif select == "2":
                result = values[0] - sum(values[1:])
            elif select == "3":
                result = math.prod(values)
            elif select == "4":
                result = values[0] / math.prod(values[1:])

            print("\n The result is: " + str(result) + "\n")

        except ValueError:
            print("\n Oops! Please enter a valid number of values.\n")

    elif select == "5":
        value1 = input("\n First Value: ")
        value2 = input("\n Second value: ")

        try:
            value1 = float(value1)
            value2 = float(value2)
            print("\n The result is: " + str(value1 % value2) + "\n")
        except ValueError:
            print("\n Oops! Please enter valid numeric values.\n")

    elif select == "6":
        value1 = input("\n Base Value: ")
        value2 = input("\n Exponent Value: ")

        try:
            value1 = float(value1)
            value2 = float(value2)
            print("\n The result is: " + str(math.pow(value1, value2)) + "\n")
        except ValueError:
            print("\n Oops! Please enter valid numeric values.\n")

    elif select == "7":
        value = input("\n Value: ")

        try:
            value = float(value)
            print("\n The result is: " + str(math.sqrt(value)) + "\n")
        except ValueError:
            print("\n Oops! Please enter a valid numeric value.\n")

    elif select == "8":
        value = input("\n Value: ")
        base = input("\n Base (10, e, or 2): ")

        try:
            value = float(value)

            if base == "10":
                print("\n The result is: " + str(math.log10(value)) + "\n")
            elif base == "e":
                print("\n The result is: " + str(math.log(value)) + "\n")
            elif base == "2":
                print("\n The result is: " + str(math.log2(value)) + "\n")
            else:
                print("\n Invalid base value! Please choose 10, e, or 2.\n")

        except ValueError:
            print("\n Oops! Please enter a valid numeric value.\n")

    elif select == "9":
        value = input("\n Value: ")

        try:
            value = float(value)
            print("\n The result is: " + str(math.sin(value)) + "\n")
        except ValueError:
            print("\n Oops! Please enter a valid numeric value.\n")

    elif select == "10":
        value = input("\n Value: ")

        try:
            value = float(value)
            print("\n The result is: " + str(math.cos(value)) + "\n")
        except ValueError:
            print("\n Oops! Please enter a valid numeric value.\n")

    elif select == "11":
        value = input("\n Value: ")

        try:
            value = float(value)
            print("\n The result is: " + str(math.tan(value)) + "\n")
        except ValueError:
            print("\n Oops! Please enter a valid numeric value.\n")

    else:
        print("\n Oops! Please check the input you entered.\n")

    back = input("\n Do you want to go back to the main menu? (y/n) ")

    if back != 'y':
        break
