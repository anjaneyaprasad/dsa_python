def get_max_profit(price):

    """
    Given the prices for rod pieces of every size between 1 inch and n inches,
    find the maximum total profit that can be made by cutting an n inches long rod inch into pieces.
    """

    L = len(price)
    dp = [-1] * (L + 1)
    dp[0] = 0

    for l in range(1, L + 1):
        dp[l] = 0
        for cut in range(l):
            dp[l] = max(dp[l], price[cut] + dp[l - cut - 1])
    return dp[L]


# price = [1, 5, 8, 9]
# print(get_max_profit(price))
#
# price = [2, 5, 7, 8]
# print(get_max_profit(price))

price = [3, 5, 8, 9, 10, 17, 17, 20]
print(get_max_profit(price))


# def get_maximum_profit(price):
#     """
#     Args:
#      price(list_int32)
#     Returns:
#      int32
#     """
#     # Write your code here.
#     n = len(price)
#     cut_options = [0] * n
#
#     for i in range(0, n):
#         divisions = n // (i + 1)
#         remainder = n % (i + 1)
#         cut_options[i] = (divisions * price[i])
#
#         if remainder > 0:
#             cut_options[i] += price[remainder - 1]
#
#     return max(cut_options)