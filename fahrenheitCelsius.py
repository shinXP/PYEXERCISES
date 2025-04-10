while True:
    print("\n\tPlease Choose Temperature:")
    print("\t1. Celsius to Fahrenheit")
    print("\t2. Fahrenheit to Celsius")
    print("\t0. Exit")

    choice = int(input("\n\tEnter your choice: "))

    if choice == 1:
        celsius = float(input("\tEnter the temp: "))
        fahrenheit = (celsius*9/5) + 32
        print(f"\t{celsius}°C is equivalent to {fahrenheit:.2f}°F")
        break

    elif choice == 2:
        fahrenheit = float(input("\tEnter the temp: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"\t{fahrenheit}°F is equivalent to {celsius}°C")
        break

    elif choice == 0:
        print("\tEheyy")
        break

    else:
        print("\tInvalid Input")
        break