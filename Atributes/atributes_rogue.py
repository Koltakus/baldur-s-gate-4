#import pytest
import random
#@pytest.mark.parametrize(('health_rogue', 'armor_rogue', 'ulta_rogue'))
health_random_d8 = random.randint(1,8)
health_bar = health_random_d8 * '❤'
armor_random_d12 = random.randint(1,12)
armor_bar = armor_random_d12 * '🛡'
ulta_random_d8 = random.randint(1,8)
ulta_bar = ulta_random_d8 * '☩'

print('Ивое здоровье составляет: ' + health_bar)
print('Твой класс брони составляет: ' + armor_bar)
print('Время до применения ульты составляет: ' + ulta_bar)
health_rogue = []
for x in range(1, health_random_d8):
    health_rogue = []
    for y in range(health_random_d8):
        health_rogue.append('❤')
print(health_rogue)

armor_rogue = []
for x in range(1, armor_random_d12):
    armor_rogue = []
    for y in range(armor_random_d12):
        armor_rogue.append('🛡')
print(armor_rogue)

ulta_rogue = []
for x in range(1, ulta_random_d8):
    ulta_rogue = []
    for y in range(ulta_random_d8):
        ulta_rogue.append('☩')
print(ulta_rogue)


