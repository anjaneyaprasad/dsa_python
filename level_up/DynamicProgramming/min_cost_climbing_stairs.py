def min_cost_climbing_stairs(cost):
    """
    Args:
     cost(list_int32)
    Returns:
     int32
    """

    n = len(cost)
    print("length of cost : " + str(n))

    table = [-1 for _ in range(n + 2)]
    print("length of table: " + str(len(table)))

    cost.insert(0, 0) # insert 0 at index 0 ==> cost.insert(index, value)
    cost.append(0)
    m = len(cost)
    print("length of cost : " + str(m))
    table[0] = 0
    table[1] = cost[1]
    for i in range(2, n + 2):
        print("i : " + str(i))
        table[i] = cost[i] + min(table[i - 1], table[i - 2])

    return table[n + 1]


# cost = [1, 1, 2]  # 1
# cost = [12, 1, 23, 123, 45, 34, 12]  # 81
# cost = [0, 0, 999, 1]  # 1
# cost = [100, 1]  # 1
cost = [0, 1, 2] # 1
# cost = [20, 0, 0, 1]  # 0
print(min_cost_climbing_stairs(cost))