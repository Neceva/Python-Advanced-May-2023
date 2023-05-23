number_commands = int(input())
parking_data = set()

for _ in range(number_commands):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking_data.add(car_number)
    else:
        parking_data.remove(car_number)

if parking_data:
    print(*parking_data, sep="\n")
else:
    print("Parking Lot is Empty")