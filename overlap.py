import random

a = random.sample(range(100), 20)
b = random.sample(range(100), 20)

common = [num for num in a if num in b]
print(common)