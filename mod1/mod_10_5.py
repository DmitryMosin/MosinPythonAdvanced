A = [1, 2, 3, 3, 3, 5]
x = 3


def find_insert_position(lst, b):
    
    len_lst = len(lst)
    curr_i = round(len_lst / 2)
    max_i = len_lst - 1
    min_i = 0
    
    if len_lst == 0:
        lst = [b]
    if b <= lst[0]:
        return 0
    if b > lst[len(lst) - 1]:
        return len(lst)

    while max_i - min_i != 1:
        if b <= lst[curr_i]:
            max_i = curr_i
            curr_i = curr_i - round((curr_i - min_i)/2)
        else:
            min_i = curr_i
            curr_i = curr_i + round((max_i - curr_i + 1) / 2)

    return curr_i


print(find_insert_position(A, x))
