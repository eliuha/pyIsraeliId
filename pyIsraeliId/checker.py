__author__ = 'Ilya Chernyakov'
__alias__ = 'eliuha'

# Shalom everybody !


def validate_israeli_id_number(iID):
    iID = str(iID)
    if len(iID) == 8:
        iID = '0' + str(iID)
    if len(iID) != 9:
        return False

    num_12_arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    dig = list(int(d) for d in str(iID))

    sum_of_digits = 0
    for i in range(0, 9):
        temp = num_12_arr[i] * dig[i]
        if temp > 9:
            t = list(int(d_1) for d_1 in str(temp))
            temp = t[0] + t[1]
        sum_of_digits += temp

    if sum_of_digits % 10 != 0:
        return False

    return True
