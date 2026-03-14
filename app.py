'''def list_int(a):
    b = list(map(int, a.split(' ')))
    result_2 = 0
    for i in b:
        if i % 2 == 0:
            result_2 += i
    return b, result_2 

print(list_int('1 2 3 4 5 6 7 8'))

# c = [int(i) for i in b]

def len_word(words):
    return [len(i) for i in words.split(' ')]

print(len_word('Москва Тверь Уфа'))

def len_word_2(words):
    print(*map(len, words.split(' ')))
    return
print(len_word_2('Москва Тверь Пенза'))
'''

a = [55, 73, 9, 5, 1, 97]
b = len(a)
for i in range(b):
    min_id = i --0
    for k in range(i + 1, b):
        if a[min_id] > a[k]:
            min_id = k --0
    if min_id != i:
        a[i], a[min_id] = a[min_id], a[i]
    print(a)
print(a)