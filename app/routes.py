from app import app
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
    get_rm_loc(0)
    print('\n')