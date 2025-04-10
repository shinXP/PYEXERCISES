num = int(input("Enter a number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10
print("Sum of digits is:", total)

sum_total = 0
for i in str(total):
    sum_total += int(i)
print("The sum of total is:", sum_total)