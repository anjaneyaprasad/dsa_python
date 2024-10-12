def set_matrix_zeros(matrix: list[list[int]]):
    cols = []
    rows = []

    print(len(matrix))
    print(len(matrix[0]))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                cols.append(j)
                rows.append(i)

    print(cols)
    print(rows)
    for j in cols:
        for i in range(len(matrix)):
            matrix[i][j] = 0

    for i in rows:
        matrix[i] = [0]*len(matrix[0])


# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
set_matrix_zeros(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])