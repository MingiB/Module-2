# the2nd_l07_12_practice
"""
1. Дан API, генерирующий случайного человека (https://pipl.ir/v1/getPerson).
2. В переменную data сохранены 10 случайных людей.
3. Используя min и lambda, найдите самого младшего человека. Сохраните его в переменную min_age_person и выведите на экран.
4. Используя max и lambda, найдите самого высокого человека ('height'). Сохраните его в переменную max_height_person и выведите на экран.
* 5. Используя reduce, lambda и любые другие функции найдите среднюю зарплату ('salary') для всех полученных людей. Сохраните его в переменную average_salary и выведите на экран.
"""

import requests
from functools import reduce
from pprint import pprint
BASE_URL = "https://pipl.ir/v1/getPerson"

data = [requests.get(BASE_URL).json() for i in range(10)]
#pprint(data)

# Ваш код здесь
f_age = lambda x:x['person']['personal']['age']
min_age_person = min([f_age(i) for i in data])
print("min_age_person")
pprint(min_age_person)

f_height = lambda x:x['person']['personal']['height']
print("max_height_person")
max_height_person = max([f_height(i) for i in data])
pprint(max_height_person)

f_salary = lambda x:float(x['person']['work']['salary'][1::])
print("average_salary")
average_salary = [f_salary(i) for i in data]
print(sum(average_salary)/len(average_salary))
