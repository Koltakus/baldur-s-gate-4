

print('Введите свое имя, Игорок 1')
player1_name = input()
print('Приветствуем тебя,' + player1_name)
print('Введите свое имя, Игорок 2')
player2_name = input()
print('Приветствуем тебя,' + player2_name)

print('Выберите класс своего персонажа,' + player1_name + '!' + '\nВыбери из предложенных ниже классов')
print('Warrior'+'\nRouge'+'\nWizard')
player1_class = input()
def player1_class_choice(player_class):
    if player_class == 'Warrior':
        player_class = 'Warrior'
    elif player_class == 'Rogue':
        player_class = 'Rogue'
    elif player_class == 'Wizard':
        player_class = 'Wizard'
    else:
        print('Вы ввели несуществующий класс персонажа')
    return player_class

player1_class = player1_class_choice(player1_class)

print(player1_name + ', ты выбрал класс ' + player1_class+'.' + '\nТы уверен в своем выборе?' + '\nДа/Нет?')


