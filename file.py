# file.py

file = open('test.log', 'r', encoding='utf8')
sizeLimits = 209715200 # byte ==200m
position = 0

lines = file.readlines(sizeLimits)

try:
    while not file.tell() - position < 0:
        position = file.tell()
    else:
