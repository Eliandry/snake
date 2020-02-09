import json
import pickle
my_favourite_group = {
    'name':'Nirvana',
    'tracks': ['rape me, about girl'],
    'albums': ['ddd','sss']
}
g = json.dumps(my_favourite_group)
print(g)
print(type(g))
with open('group_js', 'w' , encoding='utf-8') as f:
    json_music = json.dump(my_favourite_group, f)


s=pickle.dumps(my_favourite_group)
print(s)
print(type(s))
with open('group_pickle' ,'wb') as t:
    pickle_music = pickle.dump(my_favourite_group, t)