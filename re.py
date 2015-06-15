# re.py

import re

if __name__ == '__main__':
    addr = "100 BROAD ROAD APT.3"
    print(re.sub("ROAD", 'RD', addr))
    print(re.sub(r"\bROAD\b", 'rd', addr))
    pattern = '.*B.*(ROAD)?'
    print(re.search(pattern, 'ROAD'))
    print(re.search(pattern, 'B'))
    print(re.search(pattern, 'B').group())
