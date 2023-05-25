n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

first_diagonal = [matrix[index][index] for index in range(len(matrix))]
second_diagonal = [matrix[index][n - 1 - index] for index in range(len(matrix))]

diff = abs(sum(first_diagonal) - sum(second_diagonal))

print(diff)

