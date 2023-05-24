rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
max_sum = float("-inf")
submatrix = ""

for row in range(rows-1):
    for col in range(cols-1):
        current_el = matrix[row][col]
        el_below = matrix[row+1][col]
        next_el = matrix[row][col+1]
        diagonal_el = matrix[row+1][col+1]

        current_sum = current_el + el_below + next_el + diagonal_el
        if current_sum > max_sum:
            max_sum = current_sum
            submatrix = [[current_el, next_el], [el_below, diagonal_el]]

print(*submatrix[0])
print(*submatrix[1])
print(max_sum)