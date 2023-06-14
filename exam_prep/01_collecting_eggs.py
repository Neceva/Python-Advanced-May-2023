from collections import deque
MAX_BOX_SIZE = 50

eggs_sizes = deque(int(x) for x in input().split(', '))
paper_sizes = deque(int(x) for x in input().split(', '))

eggs_in_box = 0

while eggs_sizes and paper_sizes:

    first_egg = eggs_sizes.popleft()

    if first_egg <= 0:
        continue
    if first_egg == 13:
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue
    last_paper = paper_sizes.pop()

    current_sum = first_egg + last_paper

    if current_sum <= MAX_BOX_SIZE:
        eggs_in_box += 1

if eggs_in_box > 0:
    print(f"Great! You filled {eggs_in_box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(egg) for egg in eggs_sizes)}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(paper) for paper in paper_sizes)}")