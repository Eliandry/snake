import random

def play(count=0, count_bot=0, winner=0, winner_bot=0):
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(koloda)
    while True:
        choise = input('будете брать карту y/n\n')
        if choise == 'y':
            current = koloda.pop()
            random.shuffle(koloda)
            current_bot = koloda.pop()
            print('вам попалась карта достоинством %d' % current)
            print('боту попалась карта достоинством %d' % current_bot)
            count += current
            count_bot += current_bot
            table = {'ваш счет:': count, 'счет бота:': count_bot, 'количество побед:': winner,
                     'количество побед бота:': winner_bot}
            if count > 21:
                print('вы проиграли')
                print(table)
                return

            elif count_bot > 21:
                print('бот проиграл')
                print(table)
                return

            elif count == 21:
                print('Поздравляю, вы набрали 21!')
                print(table)
                return

            elif count_bot == 21:
                print('бот набрал 21')
                print(table)
                return

            end = 21 - count
            end_bot = 21 - count_bot
            if end < end_bot:
                print('вы победили')
                winner += 1
            elif end > end_bot:
                print('бот победил')
                winner_bot += 1

        else:
            print('У вас %d очков и вы закончили игру.' % count)


while True:
    re = input('будете играть?:y/n\n')
    if re == 'y' or re == 'yes' or re == 'да':
        play()
    else:
        print('ну как хотите')
        break
