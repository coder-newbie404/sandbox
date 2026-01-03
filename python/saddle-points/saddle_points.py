def saddle_points(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("irregular matrix")
        
    saddle_points = []

    for i in range(num_rows):
        for j in range(num_cols):
            element = matrix[i][j]
            is_row_max = all(element >= matrix[i][k] for k in range(num_cols))
            is_col_min = all(element <= matrix[k][j] for k in range(num_rows))

            if is_row_max and is_col_min:
                saddle_points.append({"row": i + 1, "column": j + 1})

    return saddle_points