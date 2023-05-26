import requests as r
from random import randint
from .models import Character, Location, RawStory

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
        if data['height'] != 'unknown':
            cen = int(data['height'])*.0328084
            h = str(round(cen, 2))
        else:
            h = 'unknown'
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
        
    
def get_rm_char(id):
    if id == 0:
        id = randint(1, 827)
    rm_char = Character.query.get(f"rm{id}")
    if rm_char:
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

        return rm_char

def get_poke_char(id):
    if id == 0:
        id = randint(1, 999)
    poke_char = Character.query.get(f"poke{id}")
    if poke_char:
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

        return poke_char
    
def get_dis_char(id):
    if id == 0:
        id = randint(1, 7250)
    dis_char = Character.query.get(f"dis{id}")
    if dis_char:
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

    return dis_char

def get_got_char(id):
    if id == 0:
        id = randint(1, 53)
    got_char = Character.query.get(f"got{id}")
    if got_char:
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

    return got_char


def help_get_sw_res(st):
    if not st:
        return 'None'
    ret = ''.join([get_sw_char(int(s)).full_name + ' | ' for s in st.split()])[:-3]
    return ret
    
def get_sw_loc(id):
    if id == 0:
        id = randint(1, 60)
    sw_loc = Location.query.get(f"sw{id}")
    if sw_loc:
        return sw_loc
    res = r.get(f'https://swapi.dev/api/planets/{id}')
    data = res.json()
    loc_id = 'sw' + str(id)
    loc_uni = "Star Wars"
    loc_name = data['name']
    if data['diameter'] != 'unknown':
        dia = str(int(float(data['diameter'])*.621371))
    else:
        dia = 'unknown'
    loc_desc = f"A {data['terrain']} planet with {data['rotation_period']} hours in the day and {data['orbital_period']} days in a year.  {dia} Miles in diameter with a population of {data['population']}."
    resident_ids = ' '.join([r[29:].rstrip("/") for r in data['residents'] if data['residents']])
    loc_residents = help_get_sw_res(resident_ids)
    sw_loc = Location(loc_id, loc_uni, loc_name, loc_desc, loc_residents)
    sw_loc.saveLoc()
    print(sw_loc.to_dict())
    return sw_loc


def help_get_rm_res(st):
    if not st:
        return 'None'
    ret = ''.join([get_rm_char(int(s)).full_name + ' | ' for s in st.split()])[:-3]
    return ret    

def get_rm_loc(id):
    if id == 0:
        id = randint(1, 127)
    rm_loc = Location.query.get(f"rm{id}")
    if rm_loc:
        return rm_loc
    res = r.get(f'https://rickandmortyapi.com/api/location/{id}')
    data = res.json()
    loc_id = 'rm' + str(id)
    loc_uni = "Rick and Morty"
    loc_name = data['name']
    loc_desc = f"A {data['type']} in {data['dimension']}"
    resident_ids = ' '.join([r[42:].rstrip("/") for r in data['residents'] if data['residents']])
    loc_residents = help_get_rm_res(resident_ids)
    rm_loc = Location(loc_id, loc_uni, loc_name, loc_desc, loc_residents)
    rm_loc.saveLoc()
    print(rm_loc.to_dict())
    return rm_loc

def get_story(id):
    if id == 0:
        id = randint(1, 5)
    story = RawStory.query.get(id)

    return story.rstring, story.id

def get_story_deets(st):
    s = st[0]
    key = {}
    l= 0
    r = None
    while l < len(s):
        if s[l] == '{':
            if not r:
                r = l + 1
        if s[l] == '{' and s[r] != '}':
            r += 1
        elif s[l] == '{' and s[r] == '}':
            x = s[l+2:r-1]
            if x not in key:
                key[x] = 1
            else:
                key[x] +=1
            l = r + 1
            r = None
        else:
            l +=1
    c = 0
    l = 0
    for x in key:
        if x[0] == 'C':
            c += 1
        elif x[0] == 'L':
            l += 1
    key['chars'] = c
    key['locs'] = l
    return key, st[1]
