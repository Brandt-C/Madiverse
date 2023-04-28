from flask import Blueprint, request

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