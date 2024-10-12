from collections import deque


def can_be_divided(num_of_people, dislike1, dislike2):
    '''
    a graph is bipartite if it does not contain odd length cycle.
    '''

    adj_list = [[] for _ in range(num_of_people)]
    visited = set()
    parent = [-1] * num_of_people
    distance = [0] * num_of_people
    queue = deque()

    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])

    def bfs(src, visited, parent, distance, adj_list):
        visited.add(src)
        queue.append(src)
        parent[src] = -1
        distance[src] = 0

        while queue:
            node = queue.popleft()
            for ngb in adj_list[node]:
                if ngb not in visited:
                    visited.add(ngb)
                    parent[ngb] = node
                    distance[ngb] = distance[node] + 1
                    queue.append(ngb)
                elif parent[node] != ngb:  # neighbour is not source of the node
                    if distance[node] == distance[ngb]:
                        print("node: " + str(node) + " - " + str(distance[node]) + " ngb :" + str(ngb) + " - " + str(distance[ngb]))
                        print("Returning True")
                        return True

        print("returning False")
        return False

    for i in range(num_of_people):
        if i not in visited:
            if bfs(i, visited, parent, distance, adj_list):
                return False

    return True

# num_of_people = 5
# dislike1 = [0, 1, 1, 2, 3]
# dislike2 = [2, 2, 4, 3, 4]

# num_of_people = 4
# dislike1 = [0, 0, 0, 1, 2]
# dislike2 = [1, 2, 3, 2, 3]
# print(can_be_divided(num_of_people, dislike1, dislike2))

num_of_people = 4
dislike1 = [0, 0, 0, 1, 2]
dislike2 = [1, 2, 3, 2, 3]
print(can_be_divided(num_of_people, dislike1, dislike2))

# YOUR OUTPUT
# 1


#
# {
# "num_of_people": 5,
# "dislike1": [0, 1, 2, 3, 4],
# "dislike2": [1, 2, 3, 4, 0]
# }
# YOUR OUTPUT
# 1
# EXPECTED OUTPUT
# 0
#
#
# {
# "num_of_people": 8,
# "dislike1": [0, 1, 3, 3, 4, 6],
# "dislike2": [1, 2, 4, 5, 5, 7]
# }
# YOUR OUTPUT
# 1
# EXPECTED OUTPUT
# 0
#
#
# {
# "num_of_people": 5,
# "dislike1": [0, 1, 2, 3, 4],
# "dislike2": [1, 2, 3, 4, 1]
# }
# YOUR OUTPUT
# 1
# EXPECTED OUTPUT
# 1
#
#
#
# {
# "num_of_people": 7,
# "dislike1": [6, 6, 4, 4, 0],
# "dislike2": [5, 3, 3, 5, 5]
# }
# YOUR OUTPUT
# 1
# EXPECTED OUTPUT
# 1
#
