def max_win(v):
    """
    Consider a row of n coins of values v1, . . . , vn.
    We play a game against an opponent by alternating turns.
    In each turn, a player selects either the first or last coin from the row,
    removes it from the row permanently, and receives the value of the coin.
    Determine the maximum possible amount of money we can definitely win if we move first.
    Assume full competency by both players.
    """

    n = len(v)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = v[i]

    for diff in range(1, n):
        for left in range(n - diff):
            right = left + diff
            dp[left][right] = max(v[left] - dp[left + 1][right], v[right] - dp[left][right - 1])

    return dp[0][n-1] >= 1


v = [8, 15, 3, 7]
print(max_win(v))
