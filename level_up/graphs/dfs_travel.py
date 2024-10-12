def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if n == 0:
        return []
    if n != 0 and len(edges) == 0:
        return [i for i in range(n)]

    adj_list: list[list[int]] = [[] for _ in range(n)]
    visited = [0] * n
    result = []

    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    def dfs(s):
        visited[s] = 1
        result.append(s)

        for w in adj_list[s]:
            if visited[w] == 0:
                dfs(w)

    for src in range(n):
        if visited[src] == 0:
            dfs(src)

    return result


n = 6
edges = [[0, 1], [0, 2], [1, 4], [3, 5]]

print(dfs_traversal(n, edges))
