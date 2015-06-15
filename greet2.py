# greet2.py

name = 'Peter'

def greet():
    print("Hello", name)
    return

def greet_again():
    name = 'Sue'
    print('Hello', name)
    return

greet()
greet_again()
print('Hello', name)
