def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """

    # define graph
    adj_list: list[list[int]] = [[] for _ in range(n)]
    visited: list[int] = [-1] * n
    components = 0

    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    # dfs
    def dfs(node):
        visited[node] = 1

        for ngb in adj_list[node]:
            if visited[ngb] == -1:
                dfs(ngb)

    # outer loop
    for node in range(n):
        if visited[node] == -1:
            components += 1
            dfs(node)

    return components


# Ans 2
n = 5
edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
print(number_of_connected_components(n, edges))

# Ans 1
n1 = 4
edges1 = [[0, 1], [0, 3], [0, 2], [2, 1], [2, 3]]
print(number_of_connected_components(n1, edges1))
