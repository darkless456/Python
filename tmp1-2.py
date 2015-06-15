edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spams":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No " + food +"!")
print("Finally, I finished stuffing myself")