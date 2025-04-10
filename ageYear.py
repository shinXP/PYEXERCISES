import datetime

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
currentyear = datetime.datetime.now().year
needed_age = 100 - age
year = currentyear + needed_age
print(f"{name} you will turn 100 on {year}")