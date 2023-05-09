stack = []
queries_count = int(input())
for i in range(queries_count):
    current_query = [int(x) for x in input().split()]
    command = current_query[0]
    if command == 1:
        stack.append(current_query[1])
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")
