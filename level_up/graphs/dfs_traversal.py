def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    if n == 0:
        return []
    if n != 0 and len(edges) == 0:
        return [i for i in range(n)]

    result = []
    visited = [-1] * n
    adj_list: list[list[int]] = [[] for _ in range(n)]

    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    def dfs(src):
        visited[src] = 1
        result.append(src)

        for w in adj_list[src]:
            if visited[w] == -1:
                dfs(w)

    for src in range(n):
        if visited[src] == -1:
            dfs(src)

    return result

# [0, 1, 4, 2, 3, 5]
n = 6
edges = [[0, 1], [0, 2], [1, 4], [3, 5]]
print(dfs_traversal(n, edges))


# [0, 1, 3, 2]
n1 = 4
edges1 = [[0, 1], [0, 2], [1, 3], [1, 2]]
print(dfs_traversal(n1, edges1))

#
#
# {
# "n": 2,
# "edges": [
# [0, 1]
# ]
# }
#
# [0, 1]
#
#
#
# {
# "n": 8,
# "edges": [
# [0, 1],
# [1, 4],
# [2, 3],
# [5, 6],
# [6, 7],
# [5, 7]
# ]
# }
#
# [0, 1, 4, 2, 3, 5, 6, 7]
#
#
# {
# "n": 5,
# "edges": [
# ]
# }
#
# [0, 1, 2, 3, 4]