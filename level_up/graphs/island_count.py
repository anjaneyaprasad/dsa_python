def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """

    n = len(matrix)
    m = len(matrix[0])
    # window_row = [1, -1, 0, 0]
    # window_col = [0, 0, -1, 1]
    window_row = [-1, -1, -1, 0, 0, 1, 1, 1]
    window_col = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited = [[0]*m for _ in range(n)]
    island = 0

    def dfs(visited, n, m, row, col):
        if row < 0 or col < 0 or row >= n or col >= m or visited[row][col] == 1:
            return

        # print("row " + str(row))
        # print("col " + str(col))
        visited[row][col] = 1

        for i in range(4):
            new_row = row + window_row[i]
            # print(new_row)
            new_col = col + window_col[i]
            # print(new_col)

            if 0 <= new_col < m and 0 <= new_row < n and visited[new_row][new_col] == 0 and matrix[new_row][new_col] == 1:
                dfs(visited, n, m, new_row, new_col)

    # for i in range(n):
    #     for j in range(m):
    #         print(visited[i][j])

    for i in range(n):
        for j in range(m):
            print("island :" + str(island))
            print(visited[i])
            if visited[i][j] == 0 and matrix[i][j] == 1:
                island += 1
                dfs(visited, n, m, i, j)

    return island


# grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#
# grid = [
# [1, 1, 0, 0, 0],
# [0, 1, 0, 0, 1],
# [1, 0, 0, 1, 1],
# [0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1]
# ]

# grid = [
# [1, 1, 0, 0, 0],
# [0, 1, 0, 0, 1],
# [1, 0, 0, 1, 1],
# [0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1]
# ]

# grid = [[1, 1, 0],
# [1, 1, 0],
# [0, 0, 0]
# ]

# grid =[
# [0, 1],
# [1, 0]
# ]

# print(count_islands(grid))

#  1
grid = [[0, 1],
        [1, 0]]

print(count_islands(grid))


#
# {
# "matrix": [
# [1, 0],
# [0, 1]
# ]
# }
# YOUR OUTPUT
# 2
# EXPECTED OUTPUT
# 1
#
#
#
# {
# "matrix": [
# [1, 0],
# [1, 0]
# ]
# }
# YOUR OUTPUT
# 1
# EXPECTED OUTPUT
# 1
#
#
#
# {
# "matrix": [
# [1, 1, 0, 0, 0],
# [0, 1, 0, 0, 1],
# [1, 0, 0, 1, 1],
# [0, 0, 0, 0, 0],
# [1, 0, 1, 0, 1]
# ]
# }
# YOUR OUTPUT
# 6
# EXPECTED OUTPUT
# 5
#
#
#
# {
# "matrix": [
# [1, 0, 0, 0, 0, 0, 0],
# [0, 1, 0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 0, 1, 0, 0]
# ]
# }
# YOUR OUTPUT
# 5
# EXPECTED OUTPUT
# 1
#
#
#
# {
# "matrix": [
# [1],
# [1],
# [1],
# [1],
# [1],
# [1]
# ]
# }
# YOUR OUTPUT
# 1
# EXPECTED OUTPUT
# 1