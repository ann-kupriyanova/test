#a = ['Hello\n', 'world\n', 'good\n', 'day']
#with open('file_2.txt', 'r', encoding = 'utf-8') as b:
#   result = (b.read())

#print(type(result))

#Записать эту запись в файл mood_diary.txt в формате:
#[Дата] Настроение: X/5 - Комментарий

from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
mood = input('Настроение: ')
comment = input('Описание: ')
common_answer = f'[{today}] Настроение: {mood}/5 - {comment}\n'

with open('mood_diary.txt', 'a', encoding = 'utf-8') as b:
    b.write(common_answer)
print('Запись добавлена!')

with open('mood_diary.txt', 'r', encoding = 'utf-8') as c:
    result = c.readlines()[-3:]

for i in result:
    print(i.strip())


