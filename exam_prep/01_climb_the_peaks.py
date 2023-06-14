from collections import deque

peaks = deque([("Vihren", 80),("Kutelo", 90),("Banski Suhodol", 100),("Polezhan", 60),("Kamenitza", 70)])
conquered_peaks = []

daily_portions = deque(int(x) for x in input().split(', '))
daily_stamina = deque(int(x) for x in input().split(', '))

day = 0
try_ = 0

while True:

    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    elif not daily_stamina or not daily_portions or day > 7:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    element = peaks.popleft()

    difficulty_level = element[1]
    peak = element[0]

    current_daily_portion = daily_portions.pop()
    current_daily_stamina = daily_stamina.popleft()
    current_sum = current_daily_portion + current_daily_stamina

    if current_sum >= difficulty_level:
        day += 1
        conquered_peaks.append(peak)

    else:
        peaks.appendleft(element)
        day += 1


if conquered_peaks:
    print("Conquered peaks: ")
    print("\n".join(conquered_peaks))
