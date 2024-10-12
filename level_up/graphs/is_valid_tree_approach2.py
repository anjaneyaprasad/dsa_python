def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """

    # union find approach

    # init parent list with their own value
    parent = [i for i in range(node_count)]
    # init rank list with a value of 1
    rank = [1] * node_count
    # connected components starts with node_count
    components = [node_count]

    # find method for the root of a node
    # with grandparent optimization
    def find(node):
        res = node

        while res != parent[res]:
            par = parent[parent[res]]
            res = parent[par]

        return res

    # union method for two nodes
    # if they already have the same root, then there's a cycle
    def union(n1, n2):
        p1 = find(n1)
        p2 = find(n2)

        # this means cycle
        if p1 == p2:
            return False

        if rank[p1] < rank[p2]:
            p1, p2 = p2, p1

        parent[p2] = p1
        rank[p1] += rank[p2]

        components[0] -= 1
        return True

    # after union, components should be 1
    for i in range(len(edge_start)):
        if not union(edge_start[i], edge_end[i]):
            return False

    return components[0] == 1
