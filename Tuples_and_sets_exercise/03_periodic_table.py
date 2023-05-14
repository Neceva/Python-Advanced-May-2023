count_lines = int(input())
chemical_compounds = set()

for _ in range(count_lines):
    compounds = input().split()

    for el in compounds:
        chemical_compounds.add(el)

print(*chemical_compounds, sep='\n')
