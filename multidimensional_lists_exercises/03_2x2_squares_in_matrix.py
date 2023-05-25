rows, cols = [int(n) for n in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]
square_matrix_counter = 0

for row_index in range(rows-1):

    for col_index in range(cols-1):

        current_el = matrix[row_index][col_index]
        el_below = matrix[row_index+1][col_index]
        next_el = matrix[row_index][col_index+1]
        diagonal_el = matrix[row_index+1][col_index+1]

        if current_el == el_below == next_el == diagonal_el:
           square_matrix_counter += 1

print(square_matrix_counter)
