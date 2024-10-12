def count_ways_to_climb(steps, n):
    """
    There is a staircase with n steps.
    A person standing at the 0-th step wants to reach the n-th one.
    They are capable of jumping up by certain numbers of steps at a time.
    Given how the person can jump, count the number of ways they can reach the top.

    Args:
     steps(list_int32)
     n(int32)
    Returns:
     int64
    """

    table = [-1] * (n + 1)
    table[0] = 0

    for i in range(n + 1):
        for s in steps:
            if i - s >= 0:
                table[i] += table[i - s]
        table[i] += 1

    return table[n]


# 3
steps = [2, 3]
n = 7
print(count_ways_to_climb(steps, n))

# 1
# steps = [1, 2]
# n = 1
# print(count_ways_to_climb(steps, n))

# 2
# steps = [1, 2]
# n = 2
# print(count_ways_to_climb(steps, n))
