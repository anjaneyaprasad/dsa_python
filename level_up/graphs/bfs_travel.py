from collections import deque


def adjacent_list(vertices, edges1) -> list[list[int]]:
    result = [[] for _ in range(vertices)]

    for src, dst in edges1:
        result[src].append(dst)
        result[dst].append(src)

    return result


def bfs_travel(n, edges):
    if n == 0:
        return []
    if n != 0 and len(edges) == 0:
        return [i for i in range(n)]

    adj_list = adjacent_list(n, edges)
    visited = [0]*n
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


input_edges = [[0, 1], [0, 2], [0, 4], [2, 3]]
# input_edges = []
no_of_vertices = 6

# print(bfs(no_of_vertices, input_edges))

print(bfs_travel(no_of_vertices, input_edges))
