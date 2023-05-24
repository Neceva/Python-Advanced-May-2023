rows = int(input())

matrix =[[el for el in list(input())] for _ in range(rows)]

symbol = input()
current_symbol = None
symbol_found = False

for row_index in range(rows):

    if symbol_found:
        break

    for col_index in range(rows):

        current_symbol = matrix[row_index][col_index]

        if current_symbol == symbol:
            print(f"({row_index}, {col_index})")
            symbol_found = True
            break

if not symbol_found:
    print(f"{symbol} does not occur in the matrix")