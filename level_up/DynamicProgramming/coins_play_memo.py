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

    if n % 2 != 0:
        return -1

    memo = {}

    def helper(i, j):
        if i > j or i >= n or j < 0:
            return 0

        k = (i, j)
        if k in memo:
            return memo[k]

        choice1 = v[i] + min(helper(i + 2, j), helper(i + 1, j - 1))
        choice2 = v[j] + min(helper(i, j - 2), helper(i + 1, j - 1))
        memo[k] = max(choice1, choice2)
        return memo[k]
    return helper(0, n - 1)


v = [8, 15, 3, 7]
print(max_win(v))
