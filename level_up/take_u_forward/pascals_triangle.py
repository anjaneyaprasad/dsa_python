def pascals_triangle(num_rows: int):
    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]

    tri = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(tri[i-1][j-1] + tri[i-1][j])
        row.append(1)
        tri.append(row)
    return tri


print(pascals_triangle(5))
