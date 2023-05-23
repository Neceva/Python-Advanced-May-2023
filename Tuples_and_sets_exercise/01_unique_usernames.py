usernames_collection = set()
num_users = int(input())

for _ in range(num_users):
    usernames_collection.add(input())

print(*usernames_collection, sep="\n")
