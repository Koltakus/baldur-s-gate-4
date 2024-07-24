import random

random_d6 = random.randint(1,6)
health_bar = random_d6 * '❤'
random_d8 = random.randint(1,8)
armor_bar = random_d8 * '🛡'
random_d4 = random.randint(1,4)
ulta_bar = random_d4 * '☩'

print('твое здоровье составляет: ' + health_bar)
print('твой класс брони составляет: ' + armor_bar)
print('время до применения ульты составляет: ' + ulta_bar)
health_wizard = []
for x in range(1, random_d6):
    health_wizard = []
    for y in range(random_d6):
        health_wizard.append(y)
    health_wizard.append(health_wizard)
print(health_wizard)

armor_wizard = []
for x in range(1, random_d8):
    armor_wizard = []
    for y in range(random_d8):
        armor_wizard.append(y)
    armor_wizard.append(armor_wizard)
print(armor_wizard)

ulta_wizard = []
for x in range(1, random_d4):
    ulta_wizard = []
    for y in range(random_d4):
        ulta_wizard.append(y)
    ulta_wizard.append(ulta_wizard)
print(ulta_wizard)


