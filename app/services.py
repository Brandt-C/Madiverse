import requests as r
from random import randint
from .models import Character


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
    sw_char = Character.query.get(f"sw{id}")
    if sw_char:
        print(sw_char.to_dict())
        return sw_char
    else:
        res = r.get(f'https://swapi.dev/api/people/{id}')
        data = res.json()
        char_id = 'sw' + str(id)
        char_uni = 'Star Wars'
        char_first_name = first_name(data['name'])
        char_full_name = data['name']
        char_img = f'https://starwars-visualguide.com/#/characters/{id}'
        cen = int(data['height'])*.0328084
        h = str(round(cen, 2))
        if data['mass'] != 'unknown':
            w = str(int(float(data['mass'])*2.20462))
        else:
            w = 'unknown'
        if data['species']:
            sres = r.get(data['species'][0])
            sdata = sres.json()
            char_desc = f"{data['name']}, standing at {h}ft and weighing {w}lbs.  Born {data['birth_year']}, {first_name(data['name'])} is a {sdata['name']} known to speak {sdata['language']}.  Type: {sdata['classification']}. Lifespan: {sdata['average_lifespan']} years."
        else:
            char_desc = f"{data['name']}, standing at {h}ft and weighing {w}lbs.  Born {data['birth_year']}, {first_name(data['name'])} is of an unknown species."
        sw_char = Character(char_id, char_full_name, char_desc, char_img, char_first_name, char_uni)
        sw_char.saveChar()

        print(sw_char.to_dict())
        return sw_char
        

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
    rm_char = Character.query.get(f"rm{id}")
    if rm_char:
        print(rm_char.to_dict())
        return rm_char
    else:
        res = r.get(f'https://rickandmortyapi.com/api/character/{id}')
        data = res.json()
        char_id = 'rm' + str(id)
        char_uni = 'Rick and Morty'
        char_first_name = first_name(data['name'])
        char_full_name = data['name']
        char_img = data['image']
        char_desc = f"{data['name']} a {data['gender']} {data['type']} type of {data['species']} from {data['origin']['name']}, recently found: {data['location']['name']}."
        rm_char = Character(char_id, char_full_name, char_desc, char_img, char_first_name, char_uni)
        rm_char.saveChar()

        print(rm_char.to_dict())
        return rm_char

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
    poke_char = Character.query.get(f"poke{id}")
    if poke_char:
        print(poke_char.to_dict())
        return poke_char
    else:
        res = r.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
        data = res.json()
        char_id = 'poke' + str(id)
        char_uni = 'Pokemon'
        char_first_name = data['name'].title()
        char_full_name = data['name'].title()
        if data['sprites']['other']['dream_world']:
            char_img = data['sprites']['other']['dream_world']['front_default']
        elif data['sprites']['other']['official-artwork']:
            char_img = data['sprites']['other']['dream_world']['official-artwork']
        else:
            char_img = data['sprites']['front_shiny']
        res2 = r.get(f'https://pokeapi.co/api/v2/pokemon-species/{id}')
        d2 = res2.json()
        des = strip_escape_chars(d2['flavor_text_entries'][0]['flavor_text'])
        char_desc = f"{data['name'].title()}- {des}."
        poke_char = Character(char_id, char_full_name, char_desc, char_img, char_first_name, char_uni)
        poke_char.saveChar()

        print(poke_char.to_dict())
        return poke_char
    

# NEW ADDS

def get_dis_char(id):
    if id == 0:
        id = randint(1, 7250)
    dis_char = Character.query.get(f"dis{id}")
    if dis_char:
        print(dis_char.to_dict())
        return dis_char
    res = r.get(f'https://api.disneyapi.dev/character/{id}')
    data = res.json()
    char_id = 'dis' + str(id)
    char_uni = 'Disney'
    char_first_name = first_name(data['data']['name'])
    char_full_name = data['data']['name']
    char_img = data['data']['imageUrl']
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
    char_desc = f"{data['data']['name']} from {attr}."
    dis_char = Character(char_id, char_full_name, char_desc, char_img, char_first_name, char_uni)
    dis_char.saveChar()

    print(dis_char.to_dict())
    return dis_char

def get_got_char(id):
    if id == 0:
        id = randint(1, 53)
    got_char = Character.query.get(f"got{id}")
    if got_char:
        print(got_char.to_dict())
        return got_char
    res = r.get(f'https://thronesapi.com/api/v2/Characters/{id}')
    data = res.json()
    char_id = 'got' + str(id)
    char_uni = 'Game Of Thrones'
    char_first_name = data['firstName']
    char_full_name = data['fullName']
    char_img = data['imageUrl']
    char_desc = f"{data['fullName']}, {data['title']}, of: {data['family']}."
    got_char = Character(char_id, char_full_name, char_desc, char_img, char_first_name, char_uni)
    got_char.saveChar()

    print(got_char.to_dict())
    return got_char
