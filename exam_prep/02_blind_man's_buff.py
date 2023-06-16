def find_my_coordinates(r, c, matrix):
    for row in range(r):
        for col in range(c):
            if matrix[row][col] == 'B':
                return [row, col]

def check_my_next_position(my_row, my_col, current_matrix):
    if 0 <= my_row < len(current_matrix) and 0 <= my_col < len(current_matrix):
        next_position = current_matrix[my_row][my_col]
        if next_position == 'O':
            return False
        elif next_position == '-':
            return [my_row, my_col], current_matrix, 0
        elif next_position == 'P':
            current_matrix[my_row][my_col] = '-'
            return [my_row, my_col], current_matrix, 1


rows, cols = (int(x) for x in input().split())

playground = []
for _ in range(rows):
    playground.append(input().split())

my_coordinates = find_my_coordinates(rows, cols, playground)
playground[my_coordinates[0]][my_coordinates[1]] = '-'
result = False
touched_players = 0
made_moves = 0

while True:
    if touched_players == 3:
        break

    command = input()
    if command == 'Finish':
        break

    if command == 'up':
        result = check_my_next_position(my_coordinates[0] - 1, my_coordinates[1], playground)
    elif command == 'down':
        result = check_my_next_position(my_coordinates[0] + 1, my_coordinates[1], playground)
    elif command == 'right':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] + 1, playground)
    elif command == 'left':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] - 1, playground)

    if result:
        my_coordinates, playground, touches = result
        touched_players += touches
        made_moves += 1

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {made_moves}")
