def is_query (i, j):
    return r(i, j)

def permutation(n):
    per = [0] * n
    rem = list(range(1, n + 1))

    for i in range(n):
        for j in range(i + 1, n):
            result = is_query(i, j)

    return per

n = 5
result = permutation(n)
print(result)
