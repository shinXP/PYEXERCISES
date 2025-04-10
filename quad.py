a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(f"Two distinct real roots: {root1:.2f}, {root2:.2f}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root:.2f}")
else:
    print("No real roots (complex numbers)")