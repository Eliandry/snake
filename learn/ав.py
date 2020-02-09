def same(name, new_name, new_word):
    ds = len(name)
    new_name_list = 0
    new_word_list = 0
    for i in range(ds):
        if name[i] == new_name[i]:
            new_name_list += 1
        elif name[i] == new_word[i]:
            new_word_list += 1
    if new_name_list > new_word_list:
        return new_name
    else:
        return new_word


def different(name, new_name, new_word):
    name_len = len(name)
    new_name_len = len(new_name)
    new_word_len = len(new_word)
    if name_len > new_name_len or name_len < new_name_len and same(name, new_name, new_word) == new_name:
        return new_name
    elif name_len > new_word_len or name_len < new_word_len and same(name, new_name, new_word) == new_word:
        return new_word
    else:
        return None



