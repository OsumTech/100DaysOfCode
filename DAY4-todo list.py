import random
names_string = input("Give me names: ")

names = names_string.split(", ")

number = random.randint(0, 2)

print(names[number])

