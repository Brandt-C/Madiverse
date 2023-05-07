import requests as r
from random import randint

# def rand_sw_char():
#     return randint(1, 83)
# def rand_poke_char():
#     return randint(1, 999)
# def rand_rm_char():
#     return randint(1, 827)
# def rand_sw_loc():
#     return randint(1, 67)
# def rand_rm_loc():
#     return randint(1, 127)

def get_sw_char(id):
    if id == 0:
        id = randint(1, 83)
    res = r.get(f'https://swapi.dev/api/people/{id}')
    data = res.json()
    print(data)

def get_sw_loc(id):
    if id == 0:
        id = randint(1, 67)
    res = r.get(f'https://swapi.dev/api/planets/{id}')
    data = res.json()
    print(data)
    
def get_rm_char(id):
    if id == 0:
        id = randint(1, 827)
    res = r.get(f'https://rickandmortyapi.com/api/character/{id}')
    data = res.json()
    print(data)

def get_rm_loc(id):
    if id == 0:
        id = randint(1, 127)
    res = r.get(f'https://rickandmortyapi.com/api/location/{id}')
    data = res.json()
    print(data)

def get_poke_char(id):
    if id == 0:
        id = randint(1, 999)
    res = r.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = res.json()
    print(data)

