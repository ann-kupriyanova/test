'''
raw_data = [5, 8, -9, 'hello', '28', True, None, 53, 4.9]
clean_data = []
for i in raw_data:
    try:
        if int(i) > 0:
            clean_data.append(int(i))
    except (ValueError, TypeError):
        continue

print(clean_data)
'''

'''
lst = [
    {'категория': 'еда',
    'стоимость': 100},
    {'категория': 'транспорт',
    'стоимость': 20},
    {'категория': 'еда',
    'стоимость': 160}
]
result = {}
for i in lst:
    a = i['категория']
    b= i['стоимость']
    
    if a not in result:
        result[a] = b
    else:
        result[a] += b
    
    result[a] = result.get(a, 0) + b

print(result)
'''
data = [1, 10, 9, 71, 55, 82, 36, 7]
result_max = []
for i in range(1, len(data) - 1):
    if data[i] > data[i - 1] and data[i] > data[i + 1]:
        result_max.append(data[i])
print(result_max)