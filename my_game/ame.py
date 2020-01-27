import random


def uu_attack(coloda, stack):
    bot_cc = []
    if len(stack) > 5:
        for i in coloda:
            sa = card.get(i)
            bot_cc.append(sa)
        mn = min(bot_cc)
        index = bot_cc.index(mn)
        att = coloda[index]
        del coloda[index]
        pattern = att[0]

        for i in range(len(coloda)):
            if pattern in coloda[i]:
                atta = coloda[i]
                del coloda[i]
                return att, atta
        return att
    else:
        for i in coloda:
            sa = card.get(i)
            bot_cc.append(sa)
        mn = max(bot_cc)
        index = bot_cc.index(mn)
        att = coloda[index]
        del coloda[index]
        pattern = att[0]

        for i in range(len(coloda)):
            if pattern in coloda[i]:
                atta = coloda[i]
                del coloda[i]
                return att, atta


bito = []


def uu_def(attack, bot_card):
    def inside(attack, bot_card):
        deff = [i for i in bot_card if i[1] == attack[1]]
        defff = [i for i in deff if card[i] > card[attack]]
        if len(defff) == 0:
            cozz = [i for i in bot_card if i[1] == coza[1]]
            if len(cozz) == 0:
                bot_card.append(attack)
                return 'F'
            if len(cozz) == 1:

                return str(cozz)
            else:

                return str(min(cozz))
        if len(defff) == 1:
            return str(defff)
        else:
            return str(min(defff))

    if (type(attack) == str):
        fff = inside(attack, bot_card)
        return fff
    else:
        if len(attack) == 2:
            attack_1 = attack[0]
            attack_2 = attack[1]
            ff = inside(attack_1, bot_card)
            ffff = inside(attack_2, bot_card)
            if ff == 'F' or ffff == 'F':
                return 'бот взял'
            else:
                return ff, ffff
        else:
            attack_1 = attack[0]
            attack_2 = attack[1]
            attack_3 = attack[2]
            ff = inside(attack_1, bot_card)
            ffff = inside(attack_2, bot_card)
            fffff = inside(attack_3, bot_card)
            if ff == 'F' or ffff == 'F' or fffff == 'F':
                return 'бот взял'
            else:
                return ff, ffff, fffff


def attack_def(attack, deff, attack_player, deff_player):
    if card[deff]>card[attack] :
        if attack[1]==deff[1] or deff[1]==coza[1]:
            return 'бито'
    else:
        return 'неверная карта'






def coz(coz, list, dict, numbers):
    x = 0
    if coz in list:
        for i in list:
            dict[i] = numbers[x] + 900
            x += 1
    else:
        for i in list:
            dict[i] = numbers[x]
            x += 1


card = {}
x = 0

coloda = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
num = [-200, -100, 0, 100, 200, 300, 400, 500, 600]
coloda_h = ([i + 'h' for i in coloda])
coloda_d = ([i + 'd' for i in coloda])
coloda_c = ([i + 'c' for i in coloda])
coloda_s = ([i + 's' for i in coloda])
stack = (coloda_h + coloda_c + coloda_d + coloda_s)
coza = random.choice(stack)
print('козырь в этой игре: ' + coza)

coz(coza, coloda_s, card, num)
coz(coza, coloda_h, card, num)
coz(coza, coloda_c, card, num)
coz(coza, coloda_d, card, num)

random.shuffle(stack)
my_card = []
bot_card = []
for i in range(6):
    ca = stack.pop()
    my_card.append(ca)
for i in range(6):
    ca = stack.pop()
    bot_card.append(ca)
case=True
bot_case=True
while True:
    if bot_case:
        while True:
            gs = uu_attack(bot_card,stack)
            print('на вас походили картой {0}'.format(gs))
            de=input('{0} какой картой вы отобьете {1},если берете напишите "n"'.format(my_card,gs))
            print(bot_card)
            if de=='n':
                case = False
                my_card.append(gs)
                break
            else:
                fg=attack_def(gs,de,bot_card,my_card)




