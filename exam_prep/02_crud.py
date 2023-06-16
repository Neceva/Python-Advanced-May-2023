table = []
for _ in range(6):
    table.append(input().split())

first_position = input()
current_position = [int(first_position[1]), int(first_position[4])]

while True:

    command = input().split(', ')
    if "Stop" in command:
        break

    direction = command[1]
    action = command[0]

    if direction == "up":
        current_position[0] -= 1
    elif direction == "down":
        current_position[0] += 1
    elif direction == "left":
        current_position[1] -= 1
    elif direction == "right":
        current_position[1] += 1

    if action == "Create":
        value = command[2]
        if table[current_position[0]][current_position[1]] == ".":
            table[current_position[0]][current_position[1]] = value

    elif action == "Update":
        value = command[2]
        if table[current_position[0]][current_position[1]].isalpha() \
                or table[current_position[0]][current_position[1]].isdigit():
            table[current_position[0]][current_position[1]] = value

    elif action == "Delete":
        if table[current_position[0]][current_position[1]].isalpha() \
                or table[current_position[0]][current_position[1]].isdigit():
            table[current_position[0]][current_position[1]] = "."

    elif action == "Read":
        if table[current_position[0]][current_position[1]].isalpha() \
                or table[current_position[0]][current_position[1]].isdigit():
            print(table[current_position[0]][current_position[1]])

    first_position = [current_position[0], current_position[1]]

for row in table:
    print(" ".join(row))

