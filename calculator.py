a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
o = input("Select an operator (+, -, *, /, %, //): ")

if o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/':
    print(a / b)
elif o == '%':
    print(a % b)
elif o == '//':
    print(a // b)
else:
    print("Invalid Operator")