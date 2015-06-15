# if.py

people = int(input("The population is "))
cats = int(input("The amount of cats is "))
dogs = int(input("The amount of dogs is "))

if people < cats:
    print("Too many cats! The world is doomed")

if people > cats:
    print("Not many cats! The world is saved")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 20

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

print("Good Bye!")
