def check_if_eulerian_path_exists(node_count, graph_edges):
    '''
    :param node_count:
    :param graph_edges:
    :return:

     Eulerian Path: If a path that starts and ends at different vertices and pass through all edges exactly once.
     Vertices with odd degree in an Eulerian path should be TWO.

     Graph with vertices having number of odd degrees:
      DEGREE         TYPE
        0           Eulerian Cycle
        2           Eulerian path
    '''

    vertex = [0] * node_count
    for a, b in graph_edges:
        vertex[a] += 1
        vertex[b] += 1

    count_odd = 0
    for v in vertex:
        if v % 2 == 1:
            count_odd += 1
        if count_odd > 2:
            return False

    return True

# True
n = 4
edges = [[0, 1], [1, 2], [1, 3], [2, 0], [3, 2]]

# False
# n = 5
# edges = [[0, 3], [1, 2], [1, 3], [3, 2], [4, 1], [4, 2]]

print(check_if_eulerian_path_exists(n, edges))
