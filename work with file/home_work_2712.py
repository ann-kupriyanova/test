import random
password = [random.randint(10000, 99999) for i in range(20)]

result = []
cnt = 0
for i in password:
    cnt += 1
    a = 'Пароль ' + str(cnt) + ': ' + str(i) + '\n'
    result.append(a)

with open('passwords.txt', 'w', encoding = 'utf-8') as b:
    b.writelines(result)
