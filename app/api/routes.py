from flask import Blueprint, request
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
    return {
        'status' : 'ok',
        'message' : 'data has been received!'
    }


# story_setup = {
#     'c' : [],
#     'l' : [],
#     'sid' : None
# }