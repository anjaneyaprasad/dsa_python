from collections import deque


def adjacent_list(n, edges) -> list[list[int]]:
    adj_list = [[] for _ in range(n)]

    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    return adj_list


def bfs_traversal(n, edges):
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

    adj_list = adjacent_list(n, edges)
    visited = [0] * n
    result = []

    def bfs(src):
        queue = deque()
        queue.append(src)
        while queue:
            node = queue.popleft()
            result.append(node)
            for ngb in adj_list[node]:
                if visited[ngb] == 0:
                    visited[ngb] = 1
                    queue.append(ngb)

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            bfs(i)

    return result

#
#
#
# {
# "n": 6,
# "edges": [
# [0, 1],
# [0, 2],
# [0, 4],
# [2, 3]
# ]
# }
#
# [0, 1, 2, 4, 3, 5]
#
#
#
#
# "n": 4,
# "edges": [
# [0, 1],
# [0, 2],
# [1, 3],
# [1, 2]
# ]
# }
#
# [0, 1, 2, 3]
#
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
