rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

first_diagonal = [matrix[index][index] for index in range(rows)]

second_diagonal = [matrix[index][rows - 1 - index] for index in range(rows)]


print(f"Primary diagonal: {', '.join(str(el) for el in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in second_diagonal)}. Sum: {sum(second_diagonal)}")
