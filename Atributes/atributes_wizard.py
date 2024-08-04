import random

health_random_d6 = random.randint(1,6)
health_bar = health_random_d6 * '❤'
armor_random_d8 = random.randint(1,8)
armor_bar = armor_random_d8 * '🛡'
ulta_random_d4 = random.randint(1,4)
ulta_bar = ulta_random_d4 * '☩'

print('твое здоровье составляет: ' + health_bar)
print('твой класс брони составляет: ' + armor_bar)
print('время до применения ульты составляет: ' + ulta_bar)
health_wizard = []
for x in range(1, health_random_d6):
    health_wizard = []
    for y in range(health_random_d6):
        health_wizard.append('❤')
print(health_wizard)

armor_wizard = []
for x in range(1, armor_random_d8):
    armor_wizard = []
    for y in range(armor_random_d8):
        armor_wizard.append('🛡')
print(armor_wizard)

ulta_wizard = []
for x in range(1, ulta_random_d4):
    ulta_wizard = []
    for y in range(ulta_random_d4):
        ulta_wizard.append('☩')
print(ulta_wizard)


