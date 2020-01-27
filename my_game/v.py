import random

coloda = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
num = [-200, -100, 0, 100, 200, 300, 400, 500,600]
coloda_h = ([i + 'h' for i in coloda])
coloda_d = ([i + 'd' for i in coloda])
coloda_c = ([i + 'c' for i in coloda])
coloda_s = ([i + 's' for i in coloda])
stop = (coloda_h + coloda_c + coloda_d + coloda_s)
coz=random.choice(stop)
if coz is coloda_s:

    for i in coloda_s:
        cs[i] = num[x]
        x += 1
    for i in coloda_h:
        ch[i] = num[y]
        y += 1
    for i in coloda_d:
        cd[i] = num[z]
        z += 1
    for i in coloda_c:
        cc[i] = num[q]
        q += 1
    print(cc, cd, ch, cs)
