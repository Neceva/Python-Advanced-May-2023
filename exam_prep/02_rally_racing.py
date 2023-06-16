rows = int(input())
car_number = input()
start_coordinate = [0, 0]
passed_kilometers = 0

race_route = []

for _ in range(rows):
    race_route.append(input().split())


while True:
    command = input()
    if command == "End":
        race_route[start_coordinate[0]][start_coordinate[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        break
    elif command == "left":
        start_coordinate[1] -= 1
    elif command == "right":
        start_coordinate[1] += 1
    elif command == "up":
        start_coordinate[0] -= 1
    elif command == "down":
        start_coordinate[0] += 1

    row, col = start_coordinate[0], start_coordinate[1]
    passed_kilometers += 10

    if race_route[row][col] == "T":
        race_route[row][col] = "."
        passed_kilometers += 20

        for row_index in range(rows):
            for col_index in range(rows):
                if race_route[row_index][col_index] == "T":
                    start_coordinate = [row_index, col_index]
                    race_route[row_index][col_index] = "."

    if race_route[row][col] == "F":
        race_route[row][col] = "C"
        print(f"Racing car {car_number} finished the stage!")
        break


print(f"Distance covered {passed_kilometers} km.")

for row in range(len(race_route)):
    print(''.join(race_route[row]))
