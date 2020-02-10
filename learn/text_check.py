def check(name_file_1, name_file_2):
    result = {}
    with open(name_file_1, 'r') as f:
        text_1 = f.read()
    with open(name_file_2, 'r') as f:
        text_2 = f.read()
    if len(text_1) < len(text_2):
        min_text = text_1
        max_text = text_2
    else:
        min_text = text_2
        max_text = text_1
    for i in range(len(min_text)):
        if text_1[i] != text_2[i]:
            result[text_2[i]] = i
    lens = len(max_text) - len(min_text)
    return (
        'количество несоответствий {0}.  Несовпадений по длине {1}.  Список ошибок и их порядковый номер {2}'.format(
            len(result), lens, result))



