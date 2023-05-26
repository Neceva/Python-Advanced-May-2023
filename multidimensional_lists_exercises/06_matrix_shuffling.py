rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:

    comm = input().split()

    if "END" in comm:
        exit(0)

    if len(comm) == 5:

        command = comm[0]
        first_row = int(comm[1])
        first_col = int(comm[2])
        second_row = int(comm[3])
        second_col = int(comm[4])

        if command == "swap" \
                and first_row in valid_rows  \
                and second_row in valid_rows \
                and first_col in valid_cols \
                and second_col in valid_cols:

            matrix[first_row][first_col], matrix[second_row][second_col] \
                = matrix[second_row][second_col], matrix[first_row][first_col]

            [print(*matrix[row]) for row in range(rows)]

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
