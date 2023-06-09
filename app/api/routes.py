from flask import Blueprint, request, jsonify
from ..services import *
from ..models import RawStory

api = Blueprint('api', __name__, url_prefix='/api')


@api.post('/addstory')
def add_story():
    data = request.json
    new = RawStory(data['story'])
    new.saveStory()
    return {
        'status' : 'ok',
        'message' : 'Story added!'
    }

@api.get('/story/rando')
def get_rando_deets():
    rando = get_story_deets(get_story(0))
    return {
        'status' : 'ok',
        'data' : rando[0],
        'sid' : rando[1]
    }

@api.post('/getstory')
def send_story_package():
    data = request.json
    print(data)
    # x = story_setup(data)
    y = writter(data)
    print('\nwritter:\n', y)
    return {
        'status' : 'ok',
        'message' : 'data has been received!',
        'text': y
    }

@api.get('/char/rando/<uni_st>')
def get_rando_char(uni_st):
    x = char_case(uni_st)
    return {
    'status' : 'ok',
    'data' : x
    }

@api.get('/loc/rando/<uni_st>')
def get_rando_loc(uni_st):
    x = loc_case(uni_st)
    return {
    'status' : 'ok',
    'data' : x
    }

# story_setup = {
#     'c' : [],
#     'l' : [],
#     'sid' : None
# }