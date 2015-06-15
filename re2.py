# re.py

import re

text = 'JGood is a handsome boy, he is cool, clever, and so on ...'
m = re.search(r'\shan(ds)ome\s', text)
if m:
    print(m.group(0), '\n', m.group(1), '\n', m.groups())
    # m.group(N) 返回第N组括号匹配的字符。
    # m.groups() 返回所有括号匹配的字符，以tuple格式。
else:
    print('Not match')
