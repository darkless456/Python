# circle2.py

array1 = [1, 2, 5, 3, 6, 8, 4, 10] # 建立list
def rank(array):
    for i in range(len(array) - 1, 0, -1): # 从6到1间隔-1 注：“-”表示倒叙
        if array [i - 1] > array [i]:
           array [i - 1] , array [i] = array [i], array [ i - 1 ]
    return print(array)

rank(array1)
