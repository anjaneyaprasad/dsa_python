def number_of_ways(coins, amount):

    """
    Given a variety of coin denominations existing in a currency system,
    find the total number of ways a given amount of money can be expressed using coins in that currency system.
    Assume infinite supply of coins of every denomination. Return answer modulo 1000000007.
    """

    dp = [0]*(amount+1)
    dp[0] = 1

    for c in coins:
        for i in range(c, amount + 1):
            dp[i] += dp[i - c]

    return dp[amount]

coins = [1, 2, 3]
amount = 3
print(number_of_ways(coins, amount))
