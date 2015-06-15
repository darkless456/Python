# gui.py
# coding:utf-8
from tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = "Hello, world!")
        self.helloLabel.pack()
        self.quitButton = Button(self, text = "Quit", command = self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)
# 实例化
app = Application()
# 窗口标题
app.master.title("Hello World")
# 主消息循环
app.mainloop()
