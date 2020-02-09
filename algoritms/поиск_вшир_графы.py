from collections import deque

graph = {}
graph["you"] = ["alice", " ЬоЬ", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_qu = deque()  # создает очередь
    search_qu += graph[name]
    searched = []
    while search_qu:  # пока очередь не пуста
        person = search_qu.popleft()  # Извлекается первый человек
        if not person in searched:  # проверяет проверялся ли уже человек
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
        else:
            search_qu += graph[person]
            searched.append(person)
    return False

print(search('claire'))
