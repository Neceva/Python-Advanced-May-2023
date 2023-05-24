n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

diagonal = 0

for row_index in range(n):
    for col_index in range(n):
        if row_index == col_index:
            diagonal += matrix[row_index][col_index]

print(diagonal)
