with open('file_1.txt', 'w', encoding = 'utf-8') as b:
    b.writelines('Привет! Как дела? \n')
    b.writelines('Вторая строка.')

with open('file_1.txt', 'r', encoding = 'utf-8') as a:
    print(a.read())