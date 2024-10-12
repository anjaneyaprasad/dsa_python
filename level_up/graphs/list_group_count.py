n = 6
# edges = [[0, 1], [0, 2], [1, 3], [3, 0], [3, 2], [4, 3], [4, 0]]
edges = [[0, 4], [0, 5], [1, 2], [2, 3], [3, 1], [4, 3]]

# flattened list
edges1 = [j for i in edges for j in i]

# dictionary
counts = dict()
for i in edges1:
    counts[i] = counts.get(i, 0) + 1
# values_list


# check values_list has odd values, which means any of edge has odd degree.
result = False
for x in counts.values():
    if x % 2 != 0:
        result = False
        break
    else:
        result = True

print(result)


def check_if_eulerian_cycle_exists(n, edges):
    vertex = [0] * n
    for a, b in edges:
        vertex[a] += 1
        vertex[b] += 1

    for v in vertex:
        if v % 2 == 1:
            return False
    return True


print(check_if_eulerian_cycle_exists(n, edges))



#
# print(edges1)
#
# a = [1, 2, 3, 3, 1, 2]
# print(a.count(2))
#
# print(Counter(a))
#
#
# counts = dict()
# for i in a:
#     counts[i] = counts.get(i, 0) + 1
#
# result = False
# for j in counts.values():
#     if j % 2 != 0:
#         break
#     else:
#         result = True
#
# print(result)
# print(counts)


'''

def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    if n == 1:
        return True
        
    edges1 = [x for i in edges for x in i]
    counts = dict()
    for i in edges1:
        counts[i] = counts.get(i, 0) + 1
    
    result = False
    for j in counts.values():
        if j % 2 != 0:
            result = False
            break
        else:
            result = True
            
    return result


'''
