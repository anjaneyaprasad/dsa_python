def max_product_from_cut_pieces(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    dp = [-1] * (n + 1)
    dp[1] = 1

    for length in range(2, n + 1):
        for cut in range(1, length):
            dp[length] = max(dp[length], max((length - cut) * cut, cut * dp[length - cut]))

    return dp[n]


# print(max_product_from_cut_pieces(4))

print(max_product_from_cut_pieces(3))
