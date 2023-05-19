from app import app
from flask import render_template
from .services import *

@app.route('/test')
def test():
    print('POKE CHAR:')
    get_poke_char(0)
    print('\n')
    print('Rick N Morty CHAR:')
    get_rm_char(0)
    print('\n')
    print('Star Wars CHAR:')
    get_sw_char(0)
    print('\n')
    print('\n')
    get_sw_loc(0)
    print('\n')
    # get_rm_loc(0)
    print('\n')
    print('DISNEY Char')
    get_dis_char(0)
    print('\n')
    
    return render_template('land.html')


@app.route('/testing')
def test2():
    print(get_story_deets(get_story(0)))
    return render_template('land.html')