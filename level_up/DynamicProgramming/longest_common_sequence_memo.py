def lcs(s1, s2, m, n):
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    if memo[m][n] != -1:
        return memo[m][n]

    if n == 0 or m == 0:
        memo[m][n] = 0
    else:
        if s1[m - 1] == s2[n - 1]:
            memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1)
        else:
            memo[m][n] = max(lcs(s1, s2, m - 1, n), lcs(s1, s2, m, n - 1))

    return memo[m][n]


s1 = "AXYZ"
s2 = "BAZ"
m = 4
n = 3

print(lcs(s1, s2, m, n))
