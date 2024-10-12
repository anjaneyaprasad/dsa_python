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
    diffs = [[0] * n for _ in range(n)]
    for i in range(n):
        diffs[i][i] = v[i]

    for row in range(n - 2, -1, -1):
        for col in range(row + 1, n):
            diffs[row][col] = max(v[row] - diffs[row + 1][col], v[col] - diffs[row][col - 1])

    full_diff = diffs[0][n - 1]
    return (full_diff + sum(v)) // 2


v = [8, 15, 3, 7]
print(max_win(v))
