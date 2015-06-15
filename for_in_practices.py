s = 'abcdefghijk'
for (i,j) in enumerate(s):
    print((i,j))


zip()
ta = {1,2,3}
tb = [9,8,7]
tc = ('a','b','c')
for (a,b,c) in zip(ta,tb,tc):
    print((a,b,c))

print('*'*50)

func = lambda x,y: x+y

re = map((lambda x,y: x+y),[1,2,3],[6,7,8])
print(tuple(re))
