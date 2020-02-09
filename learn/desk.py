import math

def check(id, id1):
    try:
        f = int(yr[id])
        ff = int(yr[id1])
    except:
        if yr[id - 1] == '-':
            return -int(yr[id])
        return yr[id]
    else:
        if yr[id - 1] == '-':
            return -int(str(yr[id]) + str(yr[id1]))
        return yr[id] + yr[id1]


def checkd(id, id1):
    try:
        f = int(yr[id])
        ff = int(yr[id1])
    except:

        return yr[id]
    else:

        return yr[id] + yr[id1]


yr = input('введите уравнение: ')
if len(yr) == 12:
    if yr[0] == 'x':
        a = 1
        b=check(5,6)
        c=check(8,9)


    else:
        a = int(yr[0])
        if yr[5]=='-':
            b = -int(yr[6])
        else:
            b = int(yr[6])
        if yr[8]=='-':
            b = -int(yr[9])
        else:
            b = int(yr[9])

else:

    a = check(0, 1)
    a_str = checkd(0, 1)
    if len(a_str) == 2:
        b_str = checkd(7, 8)
        b = check(7, 8)

    else:
        b = check(6, 7)
        b_str=checkd(6,7)
    if len(a_str) == 2:
        if len(b_str) == 2:
            c = check(11, 12)
        else:
            c = check(10, 11)
    elif len(b_str) == 2:
        c = check(10, 11)
    else:
        c = check(9, 10)

    print('a={0};b={1};c={2}'.format(a, b, c))
    a = int(a)
    b = int(b)
    c = int(c)
    d = (b ** 2) - (4 * a * c)
    print('Дискриминант равен:', d)
    if d == 0:
        print('уравнение имеет один корень')
        x = -b / 2 * a
        print('Ответ: x = ' + str(x))
    elif d > 0:
        print('уравнение имеет два корня')
        de = math.sqrt(d)
        x_1 = -b + de / 2 * a
        x_2 = -b - de / 2 * a
        print('Ответ: х1 ={0} ; x2={1}'.format(x_1, x_2))
    else:
        print('нет корней')
