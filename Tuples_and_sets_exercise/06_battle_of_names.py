number = int(input())

odd = set()
even = set()

for i in range(number):
    name = input()
    sum_values = int(sum(ord(char) for char in name) / (i + 1))

    if (sum_values % 2) == 0:
        even.add(sum_values)
    else:
        odd.add(sum_values)

if sum(odd) == sum(even):
    print(", ".join(str(x) for x in odd.union(even)))
elif sum(odd) > sum(even):
    print(", ".join(str(x) for x in odd.difference(even)))
elif sum(odd) < sum(even):
    print(", ".join(str(x) for x in odd.symmetric_difference(even)))
