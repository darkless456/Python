# dict.py

cities = {"CA":'San Francisco', "MI":'Detroit', "FL":'Jacksonville'} # 定义dict

cities['NY'] = 'New York' # 添加元素
cities['OR'] = 'Portland'

def find_city(themap, state):  # 定义函数
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities['_find'] = find_city # 把函数 find_city 放到叫做 cities 的字典中，并将其标记为 '_find'。
# '_find'是函数find_city的键

while True:
    print("State? (ENTER to quit)")
    state = input("> ")

    if not state: break

    city_found = cities['_find'](cities, state)
    # == city_found = find_city(cities, state)
    print(city_found)
