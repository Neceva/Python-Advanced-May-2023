from collections import deque
peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}

conquered_peaks = []

daily_portions = deque(int(x) for x in input().split(', '))
daily_stamina = deque(int(x) for x in input().split(', '))

day = 0
try_ = 0

while daily_portions and daily_stamina:

    for peak, difficulty_level in peaks.items():
        day += 1
        if day == 8:
            break

        current_daily_portion = daily_portions.pop()
        current_daily_stamina = daily_stamina.popleft()

        current_sum = current_daily_portion + current_daily_stamina

        if current_sum >= difficulty_level:
            conquered_peaks.append(peak)
            continue
        else:
            try_ += 1
            if try_ == 2:
                break
            continue

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks: ")
    print("\n".join(conquered_peaks))

