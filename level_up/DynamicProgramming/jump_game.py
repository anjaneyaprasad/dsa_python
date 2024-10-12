def can_reach_last_house(maximum_jump_lengths):
    """
    Given a list of maximum jump lengths from different houses,
    determine if you can reach the last house in one or more jumps starting from the first one.
    Maximum jump length of 2 from a house, for example,
    means that you can either jump to the next house or to the one after next.

    Args:
     maximum_jump_lengths(list_int32)
    Returns:
     bool
    """

    n = len(maximum_jump_lengths)
    table = [False] * n
    table[n - 1] = True

    # for i in range(n - 2, -1, -1):
    #     j = i + maximum_jump_lengths[i]
    #     if j >= n:
    #         table[i] = True
    #     if j < n:
    #         for item in table[i: j+1]:
    #             if item:
    #                 table[i] = True
    #                 break

    for i in range(n - 2, -1, -1):
        for j in range(i, min(i + maximum_jump_lengths[i], n - 1) + 1):
            if table[j]:
                table[i] = True
                break
    return table[0]

def can_reach_last_house_v1(maximum_jump_lengths):
    """
    Args:
        maximum_jump_lengths(list_int32)
        Returns:
         bool
    """

    leftmost_success_index = len(maximum_jump_lengths) - 1

    for i in range(len(maximum_jump_lengths) - 1, -1, -1):
        if i + maximum_jump_lengths[i] >= leftmost_success_index:
            leftmost_success_index = i

    if leftmost_success_index == 0:
        return True
    return False


def can_reach_last_house_v2(maximum_jump_lengths):

    n = len(maximum_jump_lengths) - 1
    if n == 0:
        return True
    if maximum_jump_lengths[0] == 0:
        return False

    for i in range(n, -1, -1):
        if i + maximum_jump_lengths[i] >= n:
            n = i

    print(n)
    return n == 0

# maximum_jump_lengths = [3, 1, 1, 0, 2, 4]
# print(can_reach_last_house(maximum_jump_lengths))

# maximum_jump_lengths = [2, 3, 1, 0, 4, 7]
# print(can_reach_last_house(maximum_jump_lengths))

# maximum_jump_lengths = [2, 3, 1, 1, 4]
# print(can_reach_last_house(maximum_jump_lengths))

# maximum_jump_lengths = [3, 2, 1, 0, 4]
# print(can_reach_last_house(maximum_jump_lengths))


# maximum_jump_lengths = [1, 5, 2, 1, 0, 2, 0]
# print(can_reach_last_house(maximum_jump_lengths))

# maximum_jump_lengths = [2, 4, 2, 1, 0, 2, 0]
# print(can_reach_last_house(maximum_jump_lengths))

# maximum_jump_lengths = [9, 4, 2, 1, 0, 2, 0]
# print(can_reach_last_house(maximum_jump_lengths))

maximum_jump_lengths = [3, 1, 1, 0, 2, 4]
print(can_reach_last_house_v2(maximum_jump_lengths))
