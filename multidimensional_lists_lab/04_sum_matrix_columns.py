rows, cols = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split()]for _ in range(rows)]

for col_index in range(cols):

    current_sum_el = 0

    for row_index in range(rows):
        current_sum_el += matrix[row_index][col_index]

    print(current_sum_el)