# namespace.py

import time

info = 'Address: '
def func_father(country):
    start = time.clock()
    def func_son(area):
        city = 'Shanghai,'
        print(info + country + city1 + area)
        return
    city1 = 'Beijing,'
    func_son('Chaoyang')
    end = time.clock()
    print("used: ", (end - start))
    return

func_father('China,')
