def convert_edge_list_to_adjacency_matrix(n, edges):
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]

    print(len(adj_mat[0]))

    for src, dst in edges:
        adj_mat[src][dst] = 1
        adj_mat[dst][src] = 1

    return adj_mat


def main():
    edges = [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]
    n = 5
    print(convert_edge_list_to_adjacency_matrix(n, edges))


if __name__ == '__main__':
    main()
