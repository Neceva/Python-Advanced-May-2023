def initial_position(r, matrix):
    for row in range(r):
        for col in range(r):
            if matrix[row][col] == "S":
                return [row, col]


rows = int(input())

battlefield = []

for _ in range(rows):
    battlefield.append(list(input()))

submarine_position = initial_position(rows, battlefield)
battlefield[submarine_position[0]][submarine_position[1]] = "-"
hints_from_mine = 0
cruiser_destroyed = 0
next_position = None
while True:
    command = input()

    if command == "up":
        next_position = [submarine_position[0] - 1, submarine_position[1]]
    elif command == "down":
        next_position = [submarine_position[0] + 1, submarine_position[1]]
    elif command == "left":
        next_position = [submarine_position[0], submarine_position[1] - 1]
    elif command == "right":
        next_position = [submarine_position[0], submarine_position[1] + 1]

    row, col = next_position[0], next_position[1]

    if battlefield[row][col] == "*":
        battlefield[row][col] = "-"
        hints_from_mine += 1

    if hints_from_mine == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break
    if battlefield[row][col] == "C":
        battlefield[row][col] = "-"
        cruiser_destroyed += 1

    if cruiser_destroyed == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    submarine_position = next_position

battlefield[row][col] = "S"
for row in battlefield:
    print(''.join(row))