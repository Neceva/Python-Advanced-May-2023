from collections import deque

quantity_water = int(input())
names = deque([])
while True:
    name = input()
    if name == "Start":
        break
    names.append(name)

command = input().split()
while "End" not in command:
    if command[0] == "refill":
        quantity_water += int(command[1])
    else:
        get_liters = int(command[0])
        if get_liters <= quantity_water:
            print(f"{names.popleft()} got water")
            quantity_water -= get_liters
        else:
            print(f"{names.popleft()} must wait")
    command = input().split()
print(f"{quantity_water} liters left")
