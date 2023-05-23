dict = {}

for char in list(input()):

    if char not in dict.keys():
        dict[char] = 0
    dict[char] += 1

for char, num in sorted(dict.items()):
    print(f"{char}: {num} time/s", end='\n')
