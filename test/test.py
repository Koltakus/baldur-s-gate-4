import random

random_d12 = random.randint(1,12)
health_bar = random_d12 * '❤'
print(health_bar)

health_warrior = []
for x in range(1, random_d12):
    health_warrior = []
    for y in range(random_d12):
        health_warrior.append(y)
    health_warrior.append(health_warrior)
print(health_warrior)


