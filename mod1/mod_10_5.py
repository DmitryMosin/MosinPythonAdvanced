import time
x = [*range(1, 1000000)]
c = 5000


def find_insert_position_2(lst, b):
    len_lst = len(lst)

    if len_lst == 0:
        lst = [b]
    if b <= lst[0]:
        return 0
    if b > lst[len(lst) - 1]:
        return 0

    curr_i = round((len_lst)/2)
    max_i = len_lst - 1
    min_i = 0

    while max_i - min_i != 1:
        if b <= lst[curr_i]:
            max_i = curr_i
            curr_i = curr_i - round((curr_i - min_i)/2)
        else:
            min_i = curr_i
            curr_i = curr_i + round((max_i - curr_i + 1) / 2)

    return curr_i

print(find_insert_position_2(x, c))


