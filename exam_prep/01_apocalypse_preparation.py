from collections import deque

healingItems = {"Patch": 0, "Bandage": 0, "MedKit": 0}

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    summed = textile + medicament

    if summed == 30:
        healingItems["Patch"] += 1
    elif summed == 40:
        healingItems["Bandage"] += 1
    elif summed == 100:
        healingItems["MedKit"] += 1
    elif summed > 100:
        healingItems["MedKit"] += 1
        remaining_resources = summed - 100
        medicaments[-1] += remaining_resources
    else:
        medicament += 10
        medicaments.append(medicament)
if textiles:
    print("Medicaments are empty.")
elif medicaments:
    print("Textiles are empty.")
else:
    print("Textiles and medicaments are both empty.")




