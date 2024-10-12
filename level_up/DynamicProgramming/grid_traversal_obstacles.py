def number_of_paths(matrix):
    m = len(matrix)
    n = len(matrix[0])

    table = [[-1 for _ in range(n)] for _ in range(m)]

    print(len(table))
    print(len(table[0]))

    if matrix[0][0] == 0:
        table[0][0] = 0
    else:
        table[0][0] = 1

    for col in range(1, n):
        if matrix[0][col] == 0:
            table[0][col] = 0
        else:
            table[0][col] = table[0][col-1]

    for row in range(1, m):
        if matrix[row][0] == 0:
            table[row][0] = 0
        else:
            table[row][0] = table[row-1][0]

    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][col] == 0:
                table[row][col] = 0
            else:
                table[row][col] = table[row-1][col] + table[row][col-1]

    print(table)
    return table[m-1][n-1]


# matrix = [
# [1, 1, 1, 1],
# [1, 1, 1, 1],
# [1, 1, 1, 1]
# ]
# matrix = [[1, 1], [0, 1]]

matrix = [[1, 1, 1, 0, 1, 1, 1]]


print(number_of_paths(matrix))