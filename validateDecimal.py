import re
s = input("Enter a string: ")
pattern = r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$'
print("Valid decimal number" if re.match(pattern, s) else "Invalid decimal number")