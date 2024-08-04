import random

helth_random_d12 = random.randint(1,12)
health_bar = helth_random_d12 * '❤'
armor_random_d6 = random.randint(1,6)
armor_bar = armor_random_d6 * '🛡'
ulta_random_d10 = random.randint(1,10)
ulta_bar = ulta_random_d10 * '☩'

print('Твое здоровье составляет: ' + health_bar)
print('Твой класс брони составляет: ' + armor_bar)
print('Время до применения ульты составляет: ' + ulta_bar)
health_warrior = []
for x in range(1, helth_random_d12):
    health_warrior = []
    for y in range(helth_random_d12):
        health_warrior.append('❤')
print(health_warrior)

armor_warrior = []
for x in range(1, armor_random_d6):
    armor_warrior = []
    for y in range(armor_random_d6):
        armor_warrior.append('🛡')
print(armor_warrior)

ulta_warrior = []
for x in range(1, ulta_random_d10):
    ulta_warrior = []
    for y in range(ulta_random_d10):
        ulta_warrior.append('☩')
print(ulta_warrior)


