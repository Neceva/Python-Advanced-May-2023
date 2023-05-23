number_of_guests = int(input())

reservation = set()

for _ in range(number_of_guests):
    current_reservation = input()

    if len(current_reservation) == 8:
        reservation.add(current_reservation)

while True:
    guest = input()
    if guest == "END":

        print(len(reservation))
        print(*(sorted(reservation)), sep="\n")
        break

    if guest in reservation:
        reservation.remove(guest)







