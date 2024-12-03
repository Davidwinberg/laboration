def calculate_avg_temp(list):
    sum = 0
    length = 0
    for x in list:
        sum += x
        length += 1

    print(sum/length)


def when_is_spring(list):
    dagar_i_rad = 0
    index = -1
    if len(list) == 0 or sum(list) == 0:
        return index

    start = 0
    for x in list:

        index += 1


        if x > 0 and dagar_i_rad == 0:
            dagar_i_rad += 1
            start = index
        elif x > 0:
            dagar_i_rad += 1
        elif x <= 0:
            start = 0
            dagar_i_rad = 0
        else:
            dagar_i_rad = 0


        if dagar_i_rad == 7:
            return start

