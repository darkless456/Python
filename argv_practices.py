# 参数、解包、变量、运行命令

from sys import argv

script, user_name = argv # script是默认格式，开启这个脚本。是脚本本身
prompt = "> "
prompt2 = ">> "

print ("Hi %s, I'm the %s script."% (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?"% user_name)
likes = input (prompt2)
pass
print ("Where do you live %s?"% user_name)
lives = input (prompt)
pass
print ("What kind of computer do you have?")
computer = input (prompt2)
pass
print (\
'''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is .
And you have a %r computer. Nice.
'''% (likes, lives, computer))
