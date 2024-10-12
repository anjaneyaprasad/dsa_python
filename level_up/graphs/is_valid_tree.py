def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.

    visited = [-1] * node_count
    parent = [-1] * node_count

    adj_list: list[list[int]] = [[] for _ in range(node_count)]

    for i in range(len(edge_start)):
        adj_list[edge_start[i]].append(edge_end[i])
        adj_list[edge_end[i]].append(edge_start[i])

    for i in range(node_count):
        print(adj_list[i])

    def dfs(node):
        visited[node] = 1

        for ngb in adj_list[node]:
            print(str(ngb) + " - " + str(node))
            if visited[ngb] == -1:
                parent[ngb] = node
                if dfs(ngb):
                    print("returning True")
                    return True
            else:
                if ngb != parent[node]:
                    print(str(ngb) + " " + str(parent[node]) + " " + str(node) + " " + " returning True")
                    return True
        return False

    components = 0
    cycles = False

    for v in range(node_count):
        if visited[v] == -1:
            components += 1
            cycles = dfs(v)

    print(components)
    print(cycles)
    return not (components > 1 or cycles)

'''
{
"node_count": 4,
"edge_start": [0, 0, 0],
"edge_end": [1, 2, 3]
}
1


{
"node_count": 4,
"edge_start": [0, 0],
"edge_end": [1, 2]
}

0

{
"node_count": 4,
"edge_start": [0, 0, 1, 2],
"edge_end": [3, 1, 2, 0]
}

0


{
"node_count": 4,
"edge_start": [0, 0, 0, 1],
"edge_end": [1, 2, 3, 0]
}

0
'''

# 1
# node_count = 4
# edge_start = [0, 0, 0]
# edge_end = [1, 2, 3]

# 0
# node_count = 4
# edge_start = [0, 0]
# edge_end = [1, 2]

# 0
# node_count = 4
# edge_start = [0, 0, 1, 2]
# edge_end = [3, 1, 2, 0]

# 0
node_count = 4
edge_start = [0, 0, 0, 1]
edge_end = [1, 2, 3, 0]

# 1
# node_count = 6
# edge_start = [4, 4, 4, 2, 1]
# edge_end = [3, 5, 0, 0, 0]

# 1
# node_count = 4
# edge_start = [0, 2, 0]
# edge_end = [3, 1, 1]

# 1
# node_count = 4
# edge_start = [3, 2, 0]
# edge_end = [1, 0, 3]

# 1
# node_count = 6
# edge_start = [0, 0, 4, 1, 2]
# edge_end = [5, 3, 3, 0, 1]

# 1
# node_count = 6
# edge_start = [0, 0, 2, 4, 5]
# edge_end = [3, 2, 1, 2, 4]

# 0
# node_count = 4
# edge_start = [0, 0, 0, 0]
# edge_end = [1, 2, 3, 0]

# 0
# node_count = 11
# edge_start = [0, 1, 2, 3, 4, 5, 5, 7, 8, 8]
# edge_end = [1, 2, 3, 0, 5, 6, 4, 8, 9, 10]

print(is_it_a_tree(node_count, edge_start, edge_end))

# ===============================================================

# {
# "node_count": 6,
# "edge_start": [4, 4, 4, 2, 1],
# "edge_end": [3, 5, 0, 0, 0]
# }
#
# {
# "node_count": 4,
# "edge_start": [0, 2, 0],
# "edge_end": [3, 1, 1]
# }
#
# {
# "node_count": 4,
# "edge_start": [3, 2, 0],
# "edge_end": [1, 0, 3]
# }
#
#
# {
# "node_count": 6,
# "edge_start": [0, 0, 2, 1, 3],
# "edge_end": [2, 4, 1, 5, 4]
# }


# =======
#
#
# {
# "node_count": 4,
# "edge_start": [0, 0],
# "edge_end": [1, 2]
# }
#
#
# {
# "node_count": 5,
# "edge_start": [0],
# "edge_end": [3]
# }
#
# {
# "node_count": 11,
# "edge_start": [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8],
# "edge_end": [1, 2, 3, 0, 5, 6, 4, 6, 8, 9, 10]
# }


