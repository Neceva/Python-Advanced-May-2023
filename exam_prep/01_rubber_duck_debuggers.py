from collections import deque

givenDucks = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

programmers_time = deque(int(x) for x in input().split())
number_of_tasks = deque(int(x) for x in input().split())

while programmers_time and number_of_tasks:
    current_programmer_time = programmers_time.popleft()
    current_task = number_of_tasks.pop()

    calculate_time = current_programmer_time * current_task
    if 0 <= calculate_time <= 60:
        givenDucks["Darth Vader Ducky"] += 1
    elif 61 <= calculate_time <= 120:
        givenDucks["Thor Ducky"] += 1
    elif 121 <= calculate_time <= 180:
        givenDucks["Big Blue Rubber Ducky"] += 1
    elif 181 <= calculate_time <= 240:
        givenDucks["Small Yellow Rubber Ducky"] += 1

    else:
        current_task -= 2
        number_of_tasks.append(current_task)
        programmers_time.append(current_programmer_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in givenDucks.items():
    print(key + ": " + str(value))
