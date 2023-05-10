input_data = input()
indexes = []

for i in range(len(input_data)):
    char = input_data[i]
    if char == "(":
        indexes.append(i)
    elif char == ")":
        l = indexes.pop()
        print(input_data[l:i + 1])
