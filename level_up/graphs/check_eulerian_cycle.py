def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """

    '''
    Eulerian cycle: A path that starts and ends at a single vertex and passes through each edge exactly once.
      
      
           7
         l   k
       l       k     
      l          k  
     l             k 
    1 j j j j j j j 6
    a  i          h g
    a   i        h  g
    a    i      h   g
    a     i    h    g
    a      i  h     g
    a       5       g
    a      e  f     g
    a    e     f    g
    a   e       f   g
    a  e         f  g
    a e           f g
    2 d d d d d d d 4
     b              c
       b           c
         b       c
           b    c
             3
    
    If degree of every vertex is even then that graph has Eulerian Cycle. 
    So if any of vertex has odd degree then the graph can not contain Eulerian cycle.
    '''

    if n == 1:
        return True

    edges1 = [x for i in edges for x in i]

    print(edges1)
    counts = dict() # degree of every vertex
    for i in edges1:
        counts[i] = counts.get(i, 0) + 1

    print(counts)

    result = False
    for j in counts.values():
        if j % 2 != 0:
            result = False
            break
        else:
            result = True

    return result


# 1
n = 5
edges = [[0, 1], [0, 2], [1, 3], [3, 0], [3, 2], [4, 3], [4, 0]]
print(check_if_eulerian_cycle_exists(n, edges))

# 0
# n = 6
# edges = [[0, 4], [0, 5], [1, 2], [2, 3], [3, 1], [4, 3]]
# print(check_if_eulerian_cycle_exists(n, edges))
