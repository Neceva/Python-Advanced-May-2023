input_data = list(input())
indexes = []

for i in range(len(input_data)):
    if input_data[i] == "(":
        indexes.append(i)
    elif input_data[i] == ")":
        print(*input_data[indexes.pop():i + 1], sep="")
