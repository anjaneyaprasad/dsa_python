def convert_edge_list_to_adjacency_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for (src, dst) in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    for lst in adj_list:
        lst.sort()

    print(adj_list)


edges = [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]
n = 5
convert_edge_list_to_adjacency_list(n, edges)
