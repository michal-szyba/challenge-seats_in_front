def can_see_stage(seats):
        row = seats[0]
        for seat in range(len(row)):
            seats_in_front = [a[seat] for a in seats]
            print(seats_in_front)
            for place in range(len(seats_in_front)-1):
                if seats_in_front[place] < seats_in_front[place + 1]:
                    return False
        else:
            return True


print(can_see_stage([
    [7, 8, 9],
    [5, 1, 2],
    [1, 2, 1],
]))


