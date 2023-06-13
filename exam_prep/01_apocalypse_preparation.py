from collections import deque

HEALING_ITEM_THRESHOLD = 100
PATCH_THRESHOLD = 30
BANDAGE_THRESHOLD = 40

healingItems = {"Patch": 0, "Bandage": 0, "MedKit": 0}

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    summed = current_textile + current_medicament

    if summed == PATCH_THRESHOLD:
        healingItems["Patch"] += 1
    elif summed == BANDAGE_THRESHOLD:
        healingItems["Bandage"] += 1
    elif summed == HEALING_ITEM_THRESHOLD:
        healingItems["MedKit"] += 1
    elif summed > HEALING_ITEM_THRESHOLD:
        healingItems["MedKit"] += 1
        summed -= 100
        medicaments[-1] += summed
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if textiles:
    print("Medicaments are empty.")
elif medicaments:
    print("Textiles are empty.")
else:
    print("Textiles and medicaments are both empty.")

sort_result = sorted(healingItems.items(), key=lambda x: (-x[1], x[0]))

for item in sort_result:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if textiles:
    print(f"Textiles left: {(', '.join(str(el) for el in textiles))}")
if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {(', '.join(str(el) for el in medicaments))}")

