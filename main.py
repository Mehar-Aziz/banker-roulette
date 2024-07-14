import random

name_string = input("Gve everybody's names, separated by a comma. ")
names = name_string.split(", ")
random_index = random.randint(0, len(names)-1)

random_name = names[random_index]

print(f"{random_name} is going to buy today's meal")