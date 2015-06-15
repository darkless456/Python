# line_positions.py

myfile = open('myfile.txt', 'r+')
line_pos = []

mypos = myfile.tell()
line_pos.append(mypos)
line = myfile.readline()
'''
while line != '':
    mypos = myfile.tell()
    line_pos.append(mypos)
    line = myfile.readline()
'''
'''
error code:
Traceback (most recent call last):
  File "D:/python_path/line_positions.py", line 8, in <module>
    line = myfile.readline()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xbf in position 2: illegal multibyte sequence
'''
