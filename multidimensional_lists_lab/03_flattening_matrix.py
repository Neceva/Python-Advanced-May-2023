rows = int(input())

matrix = [[int(el) for el in input().split(", ")]for el in range(rows)]

flatten = []

for row in matrix:
    flatten.extend(row)

print(flatten)