# class2.py
# 重复输出laugh字符串

class Human(object):
    laugh = 'hello world'
    def show_laugh(self):
        print(self.laugh)
    def laugh_100th(self):
        for i in range(2):
            self.show_laugh()

li_lei = Human()
li_lei.laugh_100th()
