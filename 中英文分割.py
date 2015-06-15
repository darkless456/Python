def fun(a=1, b=None, c=None, *args):
    print('{0},{1},{2},{3}'.format(a, b, c, args))
      
def main():
    fun(c= 'hongten', b=2, a=[1,2,3] , *args  [3,4],[6,7])
    
if __name__ == '__main__':
    main()
