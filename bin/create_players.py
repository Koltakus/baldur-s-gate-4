#import class from class_players

print('Введите свое имя, Игорок 1')
player1_name = input()
print('Приветствуем тебя,' + player1_name)
print('Введите свое имя, Игорок 2')
player2_name = input()
print('Приветствуем тебя,' + player2_name)

print('Выберите класс своего персонажа,' + player1_name + '!' + '\nВыбери из предложенных ниже классов')
print('Warrior'+'\nRouge'+'\nWizard')
player1_class = input()
def player1_class_choice():
    if player1_class == 'Warrior':
        player1_class = 'Warrior'
    elif player1_class == 'Rogue':
        player1_class = 'Rogue'
    elif player1_class == 'Wizard':
        player1_class = 'Wizard'
    else:
        print('Вы ввели несуществующий класс персонажа')
    return player1_class

print(player1_class_choice())

