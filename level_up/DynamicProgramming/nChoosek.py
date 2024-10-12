def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    # Write your code here.
    if n < r:
        return 0

    if n == 0 or r == 0:
        return 1

    table = [[0 for _ in range(r + 1)] for _ in range(n + 1)]
    print(len(table))
    print(len(table[0]))

    for row in range(n+1):
        table[row][0] = 1
        # print(table[row][0])

    for col in range(r+1):
        table[col][col] = 1
        # print(table[col][col])

    for row in range(2, n+1):
        for col in range(1, min(row, r+1)):
            table[row][col] = table[row - 1][col] + table[row - 1][col - 1]

    return table[n][r] % (pow(10, 9) + 7)


print(ncr(200, 100))


# refer for more info: https://en.wikipedia.org/wiki/Binomial_coefficient

def nChoosek(n, r):
    if r == n or r == 0:
        return 1

    prev = 1
    k = 1
    cur = 1

    while k <= r:
        cur = (n - (k - 1)) * prev // k
        prev = cur
        k += 1
    return cur % (10**9 + 7)


