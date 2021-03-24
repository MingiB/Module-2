# the2nd_l07_11_practice
"""
1. Дан API сериала Breaking Bad (https://breakingbadapi.com/documentation).
2. В переменную data сохранены все актеры сериала.
3. Используя sorted и lambda, отсортируйте список по ключу 'name' от A до Z.
4. В итоговых данных оставьте только ключи:
    {
        'name': 'Walter White',
        'nickname': 'Heisenberg',
        'portrayed': 'Bryan Cranston',
    }
5. Результат сохраните в переменную actors и выведите на экран.
"""

import requests
from pprint import pprint
BASE_URL = "https://www.breakingbadapi.com/api/"

response = requests.get(BASE_URL + "characters/")

data = response.json()
#pprint(data)

# Ваш код здесь
actors = sorted(data, key = lambda x:x['name'])
actors = [{'name':i['name'],'nickname':i['nickname'],'portrayed':i['portrayed']}for i in actors]
pprint(actors)
