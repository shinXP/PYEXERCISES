def find_distinct_pairs(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return list(pairs)

size = int(input())

array = []

for _ in range(size):
    test_size = int(input())
    for _ in range(test_size):
        arr = list(map(int, input().split()))
        array.append(arr)
result = find_distinct_pairs(array)
print(result)