one = ['', '', '']
two = ['', '', '']
three = ['', '', '']


def player(name, sign):
    if name:
        cross_row = str(input('Введите ряд:'))
        cross_number = int(input('Введите номер:'))
        try:
            draw(cross_row, cross_number, sign)
        except:
            print('Введите коректные данные')
            player(name,sign)
        else:
            name = checker(sign)
            if name == False:
                return False
            print(' {0}\n {1}\n {2}'.format(one, two, three))


def draw(row, number, sumbol):
    global one, two, three
    rais=int(row)
    if rais>3 or number>3 :
         raise
    if row == '1':
        one[number - 1] = sumbol
    if row == '2':
        two[number - 1] = sumbol
    if row == '3':
        three[number - 1] = sumbol


def checker(nm):
    if one[0] == nm and one[1] == nm and one[2] == nm:
        return False
    elif two[0] == nm and two[1] == nm and two[2] == nm:
        return False
    elif three[0] == nm and three[1] == nm and three[2] == nm:
        return False
    elif one[0] == nm and two[0] == nm and three[0] == nm:
        return False
    elif one[1] == nm and two[1] == nm and three[1] == nm:
        return False
    elif one[2] == nm and two[2] == nm and three[2] == nm:
        return False
    elif one[0] == nm and two[1] == nm and three[2] == nm:
        return False
    elif one[2] == nm and two[1] == nm and three[0] == nm:
        return False
    else:
        return True


player_1 = True
player_2 = True
def main():
    while True:
        print('Ходит игрок 1')
        end_1 = player(player_1, 'x')
        if end_1 == False:
            print('Игрок 1 победил!')
            break
        print('Ходит игрок 2')
        end_2 = player(player_2, 'o')
        if end_2 == False:
            print('Игрок 2 победил!')
            break
main()
