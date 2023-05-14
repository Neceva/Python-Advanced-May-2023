numbers = tuple(float(x) for x in input().split())

data = {}

for num in numbers:
    if num not in data.keys():
        data[num] = 0
    data[num] += 1

for num, count in data.items():
    print(f"{num} - {count} times", end="\n")



