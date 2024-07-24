import random

random_d8 = random.randint(1,8)
health_bar = random_d8 * '❤'
random_d12 = random.randint(1,12)
armor_bar = random_d12 * '🛡'
random_d8 = random.randint(1,8)
ulta_bar = random_d8 * '☩'

print('твое здоровье составляет: ' + health_bar)
print('твой класс брони составляет: ' + armor_bar)
print('время до применения ульты составляет: ' + ulta_bar)
health_rogue = []
for x in range(1, random_d8):
    health_rogue = []
    for y in range(random_d8):
        health_rogue.append(y)
    health_rogue.append(health_rogue)
print(health_rogue)

armor_rogue = []
for x in range(1, random_d12):
    armor_rogue = []
    for y in range(random_d12):
        armor_rogue.append(y)
    armor_rogue.append(armor_rogue)
print(armor_rogue)

ulta_rogue = []
for x in range(1, random_d8):
    ulta_rogue = []
    for y in range(random_d8):
        ulta_rogue.append(y)
    ulta_rogue.append(ulta_rogue)
print(ulta_rogue)


