# coding:utf-8
# count_practices.py

def add (a, b):
    print ("Adding %d + %d"% (a, b))
    return a + b

def subtract (a, b):
    print ("Subtracting %d - %d"% (a, b))
    return a - b

def mutiply (a, b):
    print ("Mutiplying %d * %d"% (a, b))
    return a * b

def divide (a, b):
    print ("Dividing %d / %d"% (a, b))
    return a / b

print ("Let's do some math with just functions!")

age = add (30, 5)
height = subtract (78, 4)
weight = mutiply (90, 2)
iq = divide (100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d"% (age, height, weight, iq))

print ("Here is a puzzle.")

what = add (age, subtract (height, mutiply (weight, divide (iq, 2))))

print ("That becomes: ", what, "\nCan you do it by hand?")
