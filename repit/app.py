num = 107305
def best_sum_num(num):
    a = str(num)
    if len(a) % 2 == 0:
        ind = int(len(a) / 2)
        left_num = a[:ind]
        right_num = a[ind:]
        sum_1 = 0
        for i in left_num:
            sum_1 += int(i)
        sum_2 = 0
        for i in right_num:
            sum_2 += int(i)
        if sum_1 == sum_2:
            return 'Счастливый билет!'
        else:
            return 'Несчастливый билет!'

print(best_sum_num(num))