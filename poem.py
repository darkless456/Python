# poem_tang.py
# 输出古文

def func(offset=6):
    string = '静夜思 床前明月光， 疑是地上霜。 举头望明月， 低头思故乡。 唐 李白'
    a = [[' ']*offset for row in range(offset) ]
    for i in range(offset):
        for j in range(offset):
            a[i][j] = string[j + i * offset]
            b = [[r[col] for r in a[::-1]] for col in range(len(a[0]))]
            print('\n'.join(['|'.join(c for c in row) for row in b]))

func()

'''
? def func(offset=6)是什么意思？