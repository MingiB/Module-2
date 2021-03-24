# the2nd_l07_01_homework.py
"""
Для выполнения данного задания Вам потребуется зарегистрировать API на сайте https://football-data.org
После успешной регистрации Вам на почту поступит письмо:
    Your API email: your@email.com
    Your API token: <ВАШ API key>
    Your API plan: Free Tier
    
Далее Вам потребуется авторизироваться на сайте и изучить документацию:
    https://www.football-data.org/documentation/quickstart/ - как начать 
    https://www.football-data.org/documentation/api - документация API
    
Ниже приведен пример запроса GET для обработки данных чемпионатов по футболу сезона 2017-2018 гг: Англии (PL), Испании (PD), Италии (SA).
Коды чемпионатов (ссылка: www.football-data.org/documentation/api - данные внизу страницы в разделе APPENDIX):
    PL - Английская Лига
    PD - Испанская Лига
    SA - Итальянская Лига
В переменых  pl_table_row_data, pd_table_row_data, sa_table_row_data сохранены данные ответа с сервера API football-data.org - это необработанные данные, содержащие данные по итогам чемпионатов стран за 2017-2018 год.

Вам необходимо изучить содержимое этих переменных и выполнять следующие задания:
"""
import requests

API_KEY = ''
BASE_URL = 'https://api.football-data.org/v2/'
headers = {'X-Auth-Token': '84cfa2d8a9e44659a01b6bc6f8992fdb'}
filters={'season':'2019'}
path_pl = 'competitions/PL/standings' # Английская Премьер Лига
path_pd = 'competitions/PD/standings' # Испанскиа Ла Лига
path_sa = 'competitions/SA/standings' # Итальянская Серия А
response_pl = requests.get(BASE_URL + path_pl, headers=headers, params=filters)
response_pd = requests.get(BASE_URL + path_pd, headers=headers, params=filters)
response_sa = requests.get(BASE_URL + path_sa, headers=headers, params=filters)
pl_table_row_data = response_pl.json()['standings'][0]['table']
pd_table_row_data = response_pd.json()['standings'][0]['table']
sa_table_row_data = response_sa.json()['standings'][0]['table']

TABLE_HEADERS = ["POS", "TEAM", "G", "W", "D", "L", "POINTS"]

"""
1) Используя list comprehension создать список словарей для каждой лиги (PL_TABLE, PD_TABLE, SA_TABLE) состоящий из команд и ключевых параметров для каждой. Пример:
    [{'team':<НАЗВАНИЕ КОМАНДЫ>, 'position':<ПОЗИЦИЯ>, 'points': <ОЧКИ>, 'won': <ПОБЕДЫ>, 'draw': <НИЧЬИ>, 'lost': <ПОРАЖЕНИЯ>}, ..., {}] - список для каждого чемпионата должен содержать 20 команд
    
Пример каждого элемента списка: {'draw': 12, 'lost': 19, 'points': 33, 'position': 19, 'team': 'Stoke City FC','won': 7}
"""

PL_TABLE = [{'team':i['team']['name'], 'position':i['position'], 'points': i['points'], 'won': i['won'], 'draw': i['draw'], 'lost': i['lost']}for i in pl_table_row_data]
PD_TABLE = [{'team':i['team']['name'], 'position':i['position'], 'points': i['points'], 'won': i['won'], 'draw': i['draw'], 'lost': i['lost']}for i in pd_table_row_data]
SA_TABLE = [{'team':i['team']['name'], 'position':i['position'], 'points': i['points'], 'won': i['won'], 'draw': i['draw'], 'lost': i['lost']}for i in sa_table_row_data]
print("Часть 1:", PL_TABLE, PD_TABLE, SA_TABLE, sep="\n")

"""
2) Используя полученные списки PL_TABLE, PD_TABLE, SA_TABLE, необходимо получить списки словарей PL_TOP3, PD_TOP3, SA_TOP3, которые будут содержать данные только по командам с позицией <= 3. Для получения списков НЕОБХОДИМО ИСПОЛЬЗОВАТЬ lambda и filter
    Пример, для списка PL_TOP5:
        [{'team': 'Manchester City FC', 'position': 1, 'points': 100, 'won': 32, 'draw': 4, 'lost': 2}, {'team': 'Manchester United FC', 'position': 2, 'points': 81, 'won': 25, 'draw': 6, 'lost': 7}, {'team': 'Tottenham Hotspur FC', 'position': 3, 'points': 77, 'won': 23, 'draw': 8, 'lost': 7}]
"""
PL_TOP3 = list(filter(lambda x: x['position'] <= 3,PL_TABLE))
PD_TOP3 = list(filter(lambda x: x['position'] <= 3,PD_TABLE))
SA_TOP3 = list(filter(lambda x: x['position'] <= 3,SA_TABLE))
print("Часть 2:", PL_TOP3, PD_TOP3, SA_TOP3, sep="\n")

"""
3) Используя полученные списки PL_TOP3, PD_TOP3, SA_TOP3, необходимо выполнить dict comprehension для получения словарей PL_POS_T3, PD_POS_T3, SA_POS_T3 который будет содержать ключ  <НАЗВАНИЕ КОМАНДЫ> - значение <ПОЗИЦИЯ>:
    Пример для SA_POS_T3:
    {'AS Roma': 3, 'Juventus FC': 1, 'SSC Napoli': 2}
"""
PL_POS_T3 = {i['team']:i['position'] for i in PL_TOP3}
PD_POS_T3 = {i['team']:i['position'] for i in PD_TOP3}
SA_POS_T3 = {i['team']:i['position'] for i in SA_TOP3}
print("Часть 3:", PL_POS_T3, PD_POS_T3, SA_POS_T3, sep="\n")

"""
4) Далее необходимо отсортировать по позициям полученные словари PL_POS_T3, PD_POS_T3, SA_POS_T3. Для этого используйте выражения для сортировки:
    
    SORTED_SA_TOP3 = sorted(SA_POS_T3.items(), key=lambda x: x[1])

Отсортированные списки сохраните в переменные SORTED_PL_TOP3, SORTED_PD_TOP3, SORTED_SA_TOP3
"""
SORTED_PL_TOP3 = sorted(PL_POS_T3.items(), key=lambda x: x[1])
SORTED_PD_TOP3 = sorted(PD_POS_T3.items(), key=lambda x: x[1])
SORTED_SA_TOP3 = sorted(SA_POS_T3.items(), key=lambda x: x[1])
print("Часть 4:", SORTED_PL_TOP3, SORTED_PD_TOP3, SORTED_SA_TOP3, sep="\n")

"""
5) Используйте map и lambda для получения списка GROUP_BY_AWARD, который будет состоять из списков 3-х команд занявших 1 место, 3 команды занявшие 2 место, 3 команды занявшие 3 место:
    
    [['Manchester City FC', 'FC Barcelona', 'Juventus FC'],
     ['Manchester United FC', 'Club Atlético de Madrid', 'SSC Napoli'],
     ['Tottenham Hotspur FC', 'Real Madrid CF', 'AS Roma']]
"""
GROUP_BY_AWARD = list(map(lambda x,y,z: [x[0],y[0],z[0]] ,SORTED_PL_TOP3,SORTED_PD_TOP3,SORTED_SA_TOP3))
print("Часть 5:")
def msg(grouped_teams):
    try:
        for i in range(0,3):
            print(f"Команды занявшие {i+1} места: {', '.join(grouped_teams[i])}")
    except:
        print("Задание еще не выполнено")

msg(GROUP_BY_AWARD)

"""
6) Для выполнения потребуется создать новый запрос на API football-data.org:
    resp_pl_scorers, resp_pd_scorers, resp_sa_scorers (запросы написаны ниже)
    
В переменных pl_scorers_row_data, pd_scorers_row_data, sa_scorers_row_data сохранены данные ответа с сервера API football-data.org - это необработанные данные, содержащие данные по топ-10 бомбардирам чемпионатов стран за 2017-2018.

Используя dict comprehension получить словари 10 игроков в формате:
    {'Ciro Immobile': [{'nationality': 'Italy',
   'numberOfGoals': 29,
   'team': 'SS Lazio'}],
    ...,
     'Roberto Inglese': [{'nationality': 'Italy',
   'numberOfGoals': 12,
   'team': 'AC Chievo Verona'}]}
Данные сохранить в переменные PL_SCORERS, PD_SCORERS, SA_SCORERS
"""
path_pl_scorers = 'competitions/PL/scorers' # Английская Премьер Лига
path_pd_scorers = 'competitions/PD/scorers' # Испанскиа Ла Лига
path_sa_scorers = 'competitions/SA/scorers' # Итальянская Серия А
resp_pl_scorers = requests.get(BASE_URL + path_pl_scorers, headers=headers, params=filters)
resp_pd_scorers = requests.get(BASE_URL + path_pd_scorers, headers=headers, params=filters)
resp_sa_scorers = requests.get(BASE_URL + path_sa_scorers, headers=headers, params=filters)
pl_scorers_row_data = resp_pl_scorers.json()['scorers']
pd_scorers_row_data = resp_pd_scorers.json()['scorers']
sa_scorers_row_data = resp_sa_scorers.json()['scorers']

PL_SCORERS = {i['player']['name']:[{'nationality':i['player']['nationality'], 'numberOfGoals':i['numberOfGoals'], 'team':i['team']['name']}]for i in pl_scorers_row_data}
PD_SCORERS = {i['player']['name']:[{'nationality':i['player']['nationality'], 'numberOfGoals':i['numberOfGoals'], 'team':i['team']['name']}]for i in pd_scorers_row_data}
SA_SCORERS = {i['player']['name']:[{'nationality':i['player']['nationality'], 'numberOfGoals':i['numberOfGoals'], 'team':i['team']['name']}]for i in sa_scorers_row_data}
print("Часть 6:", PL_SCORERS, PD_SCORERS, SA_SCORERS, sep="\n")

"""
7) Используя set comprehension, узнать  игроки каких стран вошли в топ-10 бомбардиров каждого чемпионата. Данные сохранить для каждой лиги в виде множеств PL_NATION, PD_NATION, SA_NATION.
    Пример ответа для SA_NATION:
        {'Argentina', 'Belgium', 'Bosnia and Herzegovina', 'Croatia', 'Italy'}
"""
PL_NATION = set(i['player']['countryOfBirth'] for i in pl_scorers_row_data)
PD_NATION = set(i['player']['countryOfBirth'] for i in pd_scorers_row_data)
SA_NATION = set(i['player']['countryOfBirth'] for i in sa_scorers_row_data)
print("Часть 7:", f"PL: {PL_NATION}", f"PD: {PD_NATION}", f"SA: {SA_NATION}", sep="\n")

"""
8) Используя множества PL_NATION, PD_NATION, SA_NATION, узнать футболисты какой страны забивали в каждом чемпионате. Результат сохранить в множество NATION_TO_ALL:
    Ответ:
        {'Argentina'}
"""
NATION_TO_ALL = set(PL_NATION & PD_NATION & SA_NATION)
print("Часть 8:", NATION_TO_ALL, sep="\n")

"""
9) Используя множества PL_NATION, PD_NATION, SA_NATION, узнать футболисты какой страны забивали в чемпионате Англии (PL_NATION) чемпионате. Результат сохранить в множество ONLY_PL_NATION:
    Ответ:
        {'Algeria', 'Brazil', 'Egypt', 'England'}
"""
ONLY_PL_NATION = set()
print("Часть 9:", f"PL: {ONLY_PL_NATION}", sep="\n")

"""
10) Используя множества PL_NATION, PD_NATION, SA_NATION, узнать футболисты какой страны забивали в чемпионате Испании (PD_NATION) чемпионате. Результат сохранить в множество ONLY_PD_NATION:
    Ответ:
        {'Portugal', 'Spain', 'Uruguay', 'Wales'}
"""
ONLY_PD_NATION = set()
print("Часть 10:", f"PD: {ONLY_PD_NATION}", sep="\n")

"""
11) Используя множества PL_NATION, PD_NATION, SA_NATION, узнать футболисты какой страны забивали в чемпионате Италии (SA_NATION) чемпионате. Результат сохранить в множество ONLY_SA_NATION:
    Ответ:
        {'Bosnia and Herzegovina', 'Croatia', 'Italy'}
"""
ONLY_SA_NATION = set()
print("Часть 11:", f"SA: {ONLY_SA_NATION}", sep="\n")

"""
12)  Используя множества PL_NATION, PD_NATION, SA_NATION, узнать сколько стран представлены среди бомбардиров 3-х чемпионатов. Результат сохранить в переменную COUNT_NATION:
    Ответ:
        14
"""
COUNT_NATION = len(set())
print("Часть 12:", COUNT_NATION, sep="\n")

"""
13) Узнать, какой футболист забил больше всех остальных среди 3-х чемпионатов. Результат сохранить в переменной BEST_SCORER в виде СЛОВАРЯ. Выполнить в свободной форме (любым способом).
"""
BEST_SCORER = {}
def msg_scorer(scorer_dict):
    print("ЛУЧШИЙ БОМБАРДИР СРЕДИ ЧЕМПИОНАТОВ АНГЛИИ, ИСПАНИИ И ИТАЛИИ")
    for k, v in scorer_dict.items():
        print(f"{k.upper()} ({v[0]['team']}, {v[0]['nationality']}).\nЗА 2017-2018 год он забил {v[0]['numberOfGoals']} гол(-ов)")
print("Часть 13:")
msg_scorer(BEST_SCORER)
