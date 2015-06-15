# rename.py

import os

def trimfile(dir):
    for fn in os.listdir(dir):
        sfile = os.path.join(dir, fn)
        if os.path.isdir(sfile):
            trimfile(sfile)
            continue
        if '~' in fn:
            newfile = os.path.join(dir, fn[1:])
            open(newfile, 'wb').write(open(sfile, 'rb').read())
            print(newfile)

if __name__ == '__main__':
    trimfile(os.path.abspath('.'))
