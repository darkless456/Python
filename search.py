# search.py

import os # 引入os模块
def Search(rootDir, suffixes, arg):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir,lists)
        if os.path.isfile(path):
            if path.endswith(suffixes):
                try:
                    with open(path, encoding='utf_8') as fh:
                        lineNum = 0
                        for line in fh:
                            lineNum += 1
                            if arg in line:
                                print(lineNum, ':', path, '\n', line)

                except:
                    print('error: ', path, '\n')
        if os.path.isdir(path):
            Search(path, suffixes, arg)
Search(r'D:\python_path', ('.py', '.txt'), 'python')
