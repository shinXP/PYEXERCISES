size = list(map(int, input("Enter n: ").split()))

n = '#'
m = '.'

for i in range(size[0]):
    if (i % 2 != 0 and i % 4 != 1 and i % 4 != 2) or (size[0] < 3 and size[1] > 50):
        print("n is not odd/even")
    elif i % 2 == 0:
        print(n * size[1])
    elif i % 4 == 1:
        print(m * (size[1] - 1) + n)
    elif i % 4 == 2:
        print(n + m * (size[1] - 1))
