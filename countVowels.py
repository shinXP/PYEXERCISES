count = 0
vowels = "aeiou" or "AEIOU"
string = input("Enter a string: ")
for i in string:
	if i.lower() in vowels:
		count += 1
	elif i.upper() in vowels:
		count += 1
print(f"The number of vowels in the string is: {count}")