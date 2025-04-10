def is_prime(n):
	if n <= 1:
		return False

	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True


size = int(input("Enter the size of prime number: "))

nums = []
count = 0
while count < size:
	numbers = int(input("Enter a Number: "))
	nums.append(numbers)
	count += 1

prime_numbers = [num for num in nums if is_prime(num)]

print("The prime numbers are:", prime_numbers)
print("The sum of prime numbers are:", sum(prime_numbers))


