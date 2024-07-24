import random

random_d12 = random.randint(1,12)
health_bar = random_d12 * '❤'
random_d6 = random.randint(1,6)
armor_bar = random_d6 * '🛡'
random_d10 = random.randint(1,10)
ulta_bar = random_d10 * '☩'

print('твое здоровье составляет: ' + health_bar)
print('твой класс брони составляет: ' + armor_bar)
print('время до применения ульты составляет: ' + ulta_bar)
health_warrior = []
for x in range(1, random_d12):
    health_warrior = []
    for y in range(random_d12):
        health_warrior.append(y)
    health_warrior.append(health_warrior)
print(health_warrior)

armor_warrior = []
for x in range(1, random_d6):
    armor_warrior = []
    for y in range(random_d6):
        armor_warrior.append(y)
    armor_warrior.append(armor_warrior)
print(armor_warrior)

ulta_warrior = []
for x in range(1, random_d6):
    ulta_warrior = []
    for y in range(random_d6):
        ulta_warrior.append(y)
    ulta_warrior.append(ulta_warrior)
print(ulta_warrior)


