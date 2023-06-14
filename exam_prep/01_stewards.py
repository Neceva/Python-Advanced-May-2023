from collections import deque

seats = input().split(', ')

first_sequence = deque((int(x)) for x in input().split(', '))
second_sequence = deque((int(x)) for x in input().split(', '))

seat_matches = []
rotation_count = 0

while True:

    if len(seat_matches) == 3 or rotation_count == 10:
        print(f"Seat matches: {', '.join(seat_matches)}")
        print(f"Rotations count: {rotation_count}")
        exit(0)

    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()

    ASCII_char = chr(first_num + second_num)

    rotation_count += 1
    first_match = str(first_num) + ASCII_char
    second_match = str(second_num) + ASCII_char

    if first_match in seats:
        if first_match not in seat_matches:
            seat_matches.append(first_match)
    elif second_match in seats:
        if second_match not in seat_matches:
            seat_matches.append(second_match)
    else:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)



