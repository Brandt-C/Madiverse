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

def first_name(st):
    fn = ''
    for s in st:
        if s.isalpha():
            fn += s
        else:
            break
    return fn.title()

def get_sw_char(id):
    if id == 0:
        id = randint(1, 83)
    res = r.get(f'https://swapi.dev/api/people/{id}')
    data = res.json()
    # for images:
    # img = f'https://starwars-visualguide.com/#/characters/{id}'
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

# NEW ADDS
def get_dis_char(id):
    if id == 0:
        id = randint(1, 83)
    res = r.get(f'https://api.disneyapi.dev/character/{id}')
    data = res.json()
    print(data)

def get_dis_char(id):
    if id == 0:
        id = randint(1, 7250)
    res = r.get(f'https://api.disneyapi.dev/character/{id}')
    data = res.json()
    char = {}
    char['id'] = id
    char['uni'] = 'Disney'
    char['first_name'] = first_name(data['data']['name'])
    char['full_name'] = data['data']['name']
    char['img'] = data['data']['imageUrl']
    if data['data']['films']:
        attr = data['data']['films'][0]
    elif data['data']['shortFilms']:
        attr = data['data']['shortFilms'][0]
    elif data['data']['tvShows']:
        attr = data['data']['tvShows'][0]
    elif data['data']['videoGames']:
        attr = data['data']['videoGames'][0]
    else:
        attr = '???'
    char['desc'] = f"{data['data']['name']} from {attr}."
    print(char)

def get_got_char(id):
    if id == 0:
        id = randint(1, 53)
    res = r.get(f'https://thronesapi.com/api/v2/Characters/{id}')
    data = res.json()
    char = {}
    char['id'] = id
    char['uni'] = 'Game Of Thrones'
    char['first_name'] = data['firstName']
    char['full_name'] = data['fullName']
    char['img'] = data['imageUrl']
    char['desc'] = f"{data['fullName']}, {data['title']}, of: {data['family']}."
    print(char)
