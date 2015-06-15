# match_dna.py

def match_dna(query, sequence):
    if query in sequence:
        return True
    else:
        return False

mydna = 'gaaacctta'
myquery = 'aacc'

if match_dna(myquery, mydna):
    print('Yay it matches')
else:
    print("No it doesn't match")

# 匹配字符串 返回逻辑值
