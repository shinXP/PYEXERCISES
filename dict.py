Student = {
    "Name:": input("Enter your name: "),
    "Age:": input("Enter your age: "),
    "Height:": input("Enter your height: "),
    "Weight:": input("Enter your weight: "),
    "Adress:": input("Enter your adress: ")
}

print("\nStudent's details:")

for key, value in Student.items():
    print(key, value)
