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

def strip_escape_chars(st):
    st = repr(st)
    l = 0
    newst = ''
    while l < len(st):
        if st[l] == '\\' and st[l+1] == 'x' and st[l+2] == '0':
            l += 4
            newst += ' '
        elif st[l] == '\\':
            l += 2
            newst += ' '
        else:
            newst += st[l]
            l += 1
    return newst


def get_sw_char(id):
    if id == 0:
        id = randint(1, 83)
    print(f'SW Char--{id}')
    res = r.get(f'https://swapi.dev/api/people/{id}')
    data = res.json()
    char = {}
    char['id'] = 'sw' + id
    char['uni'] = 'Star Wars'
    char['first_name'] = first_name(data['name'])
    char['full_name'] = data['name']
    char['img'] = f'https://starwars-visualguide.com/#/characters/{id}'
    cen = int(data['height'])*.0328084
    h = str(round(cen, 2))
    if data['mass'] != 'unknown':
        w = str(int(float(data['mass'])*2.20462))
    else:
        w = 'unknown'
    if data['species']:
        sres = r.get(data['species'][0])
        sdata = sres.json()
        char['desc'] = f"{data['name']}, standing at {h}ft and weighing {w}lbs.  Born {data['birth_year']}, {first_name(data['name'])} is a {sdata['name']} known to speak {sdata['language']}.  Type: {sdata['classification']}. Lifespan: {sdata['average_lifespan']} years."
    else:
        char['desc'] = f"{data['name']}, standing at {h}ft and weighing {w}lbs.  Born {data['birth_year']}, {first_name(data['name'])} is of an unknown species."
    # for images:
    # img = f'https://starwars-visualguide.com/#/characters/{id}'
    print(char)

def get_sw_loc(id):
    if id == 0:
        id = randint(1, 60)
    print(f'location--{id}')
    res = r.get(f'https://swapi.dev/api/planets/{id}')
    data = res.json()
    loc = {}
    loc['id'] = 'sw' + id
    loc['uni'] = "Star Wars"
    loc['name'] = data['name']
    if data['diameter'] != 'unknown':
        dia = str(int(float(data['diameter'])*.621371))
    else:
        dia = 'unknown'
    loc['desc'] = f"A {data['terrain']} planet with {data['rotation_period']} hours in the day and {data['orbital_period']} days in a year.  {dia} Miles in diameter with a population of {data['population']}."
    loc['resident_ids'] = ' '.join([r[29:].rstrip("/") for r in data['residents'] if data['residents']])

    print(loc)
    
def get_rm_char(id):
    if id == 0:
        id = randint(1, 827)
    res = r.get(f'https://rickandmortyapi.com/api/character/{id}')
    data = res.json()
    char = {}
    char['id'] = 'rm' + id
    char['uni'] = 'Rick and Morty'
    char['first_name'] = first_name(data['name'])
    char['full_name'] = data['name']
    char['img'] = data['image']
    char['desc'] = f"{data['name']} a {data['gender']} {data['type']} type of {data['species']} from {data['origin']['name']}, recently found: {data['location']['name']}."
    print(data)
    print(char)

def get_rm_loc(id):
    if id == 0:
        id = randint(1, 127)
    res = r.get(f'https://rickandmortyapi.com/api/location/{id}')
    data = res.json()
    loc = {}
    loc['id'] = 'rm' + id
    loc['uni'] = "Rick and Morty"
    loc['name'] = data['name']
    loc['desc'] = f"A {data['type']} in {data['dimension']}"
    loc['resident_ids'] = ' '.join([r[42:].rstrip("/") for r in data['residents'] if data['residents']])
    print(loc)

def get_poke_char(id):
    if id == 0:
        id = randint(1, 999)
    res = r.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = res.json()
    char = {}
    char['id'] = 'poke' + id
    char['uni'] = 'Pokemon'
    char['first_name'] = data['name'].title()
    char['full_name'] = data['name'].title()
    if data['sprites']['other']['dream_world']:
        char['img'] = data['sprites']['other']['dream_world']['front_default']
    elif data['sprites']['other']['official-artwork']:
        char['img'] = data['sprites']['other']['dream_world']['official-artwork']
    else:
        char['img'] = data['sprites']['front_shiny']
    res2 = r.get(f'https://pokeapi.co/api/v2/pokemon-species/{id}')
    d2 = res2.json()
    des = strip_escape_chars(d2['flavor_text_entries'][0]['flavor_text'])
    char['desc'] = f"{data['name'].title()}- {des}."
    print(char)
    

# NEW ADDS

def get_dis_char(id):
    if id == 0:
        id = randint(1, 7250)
    res = r.get(f'https://api.disneyapi.dev/character/{id}')
    data = res.json()
    char = {}
    char['id'] = 'dis' + id
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
    char['id'] = 'got' + id
    char['uni'] = 'Game Of Thrones'
    char['first_name'] = data['firstName']
    char['full_name'] = data['fullName']
    char['img'] = data['imageUrl']
    char['desc'] = f"{data['fullName']}, {data['title']}, of: {data['family']}."
    print(char)
