player_name = input('введите имя игрока')

player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.5,
    'money': 100
}
def shopper():
    sogl = input('хотите ли вы посетить лавку торговца')
    if sogl =='да':
        while True:
            print('что вы хотите купить')
            shop = {
                20: 'зелье здоровья',
                40: 'зелье силы',
                60: 'серебрянная броня',
                110: 'алмазная броня',
                50: 'алмазная броня',
                100: 'алмазный меч'
            }
            print(shop)
            choise = int(input('сколько денег вы положите'))
            if player['money'] > choise:
                player[shop[choise]] = True
                player['money'] -= choise
                print(player)
            else:
                print('у вас недостаточно денег ')
            sogla = input('вы хотите еще что нибудь купить')
            if sogla == 'нет':
                break
    return

enemy1 = {
    'name': 'гоблин',
    'health': 50,
    'damage': 30,
    'armor': 1.0
}
enemy2 = {
    'name': 'грабитель',
    'health': 30,
    'damage': 10,
    'armor': 1.0
}
def armor_health(damage,armor):
    return damage / armor
def attack(unit, target):
    damage = armor_health(unit['damage'], target['armor'])
    target['health'] -= damage

attack(enemy1, player)
attack(player, enemy1)
print(enemy1)
print(player)

if enemy1['health'] == 0:
    player['money'] += 50
print('за убийство первого врага вы получаете 50 монет')
print(shopper())

a = input('Dас ждет захватывающее путешествие.Вы готовы?')
if a =='да':
    print('Отлично.*Вы берете все необходимое и уходите *')
else:
    print('Отказ вас не спасет,ведь вас отправляет государство. *Вы берете все необходимое и уходите *')
def vor(colic):
    x =input('В лесу на вас напал грабители. Что будете делать:нападать,откупиться')
    i=0
    if x == 'нападать':
        while i != colic:
            enemy2['health']*colic
            attack(enemy2, player)
            attack(player, enemy2)
            print(enemy2)
            player['money'] += 10
            i += 1
    else:
        player['money'] -=10*colic
        print('он украл 10 монет и скрылся')
    return