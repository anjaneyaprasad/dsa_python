import math


def minimum_coins(coins, value):
    """
    Given a variety of coin types defining a currency system,
    find the minimum number of coins required to express a given amount of money.
    Assume infinite supply of coins of every type.
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    table = [math.inf] * (value + 1)

    table[0] = 0
    for i in range(1, value + 1):
        for c in coins:
            if i - c >= 0:
                table[i] = min(table[i], table[i - c])

        table[i] += 1

    return table[value]


# 3
# coins = [1, 3, 5]
# value = 9
# print(minimum_coins(coins, value))

# 128
# coins = [1, 5, 3, 7]
# value = 888
# print(minimum_coins(coins, value))

# 52
# coins = [12, 14, 8, 6, 1, 4, 16, 2, 10, 18]
# value = 909
# print(minimum_coins(coins, value))

# 43
# coins = [22, 14, 1, 18]
# value = 889
# print(minimum_coins(coins, value))

# 3
coins = [1, 8, 9, 2, 5]
value = 15
print(minimum_coins(coins, value))
