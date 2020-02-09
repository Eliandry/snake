def wor(text, item):
    count = 0
    for i in text:
        if i == item:
            count += 1
    return count


files = input('name your file: ')
with open(files, 'w') as a:
    a.write(input())
with open(files, 'r') as f:
    text = f.read()
if text in 'а' :
    for char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        perc = 100 * wor(text, char) / len(text)
        print('{0} - {1}%'.format(char, round(perc, 2)))
else:
    for char in 'abcdefghijklmnopqrstuvwxyz':
        perc = 100 * wor(text, char) / len(text)
        print('{0} - {1}%'.format(char, round(perc, 2)))
