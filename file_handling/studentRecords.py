f = open("students.txt")
print("Initial Student Records:")
print(f.read())

f = open("students.txt", "a")
append = f.write(input("Enter the student record to append: ") + "\n")
f.close()

f = open("students.txt")
print("Updated Student Records:")
print(f.read())
f.close()