from collections import deque

caffeine_mlg = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

initial_caffeine = 0
max_caffeine = 300

while True:
    if not caffeine_mlg or not energy_drinks:
        if not energy_drinks:
            print("At least Stamat wasn't exceeding the maximum caffeine.")
        else:
            print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")

        print(f"Stamat is going to sleep with {300 - max_caffeine} mg caffeine.")
        break

    current_mlg = caffeine_mlg.pop()
    current_drink = energy_drinks.popleft()

    current_sum_caffeine = current_drink * current_mlg

    if current_sum_caffeine <= max_caffeine:
        max_caffeine -= current_sum_caffeine
    else:
        energy_drinks.append(current_drink)
        max_caffeine += 30
        if max_caffeine > 300:
            max_caffeine = 300
        if max_caffeine < 0:
            max_caffeine = 0

