__author__ = "Brent Shaw"
__copyright__ = "Copyright 2019"
__credits__ = ["Brent Shaw]
__license__ = "LGPL-3.0"
__version__ = "1.3.6"
__maintainer__ = "Brent Shaw"
__email__ = "brent@bromine.co.za"
__status__ = "Production"

from flask import render_template
from app import app

#------------------------------------------------------------------------------
#Dictionary for storing pages and clues

pages = {}
pages['1'] = '1'
pages['2'] = '2'
pages['3'] = '3'
pages['4'] = '4'
pages['5'] = '5'

#------------------------------------------------------------------------------

@app.route('/')
def start():
    '''Function displays the start page.

    Returns:
        The rendered HTML for the start page
    '''
    return render_template("index.html")

@app.route('/<T>')
def puzzle(T):
    '''Function for handling all attemps at finding pages.

    Args:
        <T>: The URL that was requested (response to clue).

    Returns:
        The rendered HTML for each clue
    '''
    try:
        n = pages[T]
        return render_template("puzzle.html", number=n, clue=pages[T])
    except:
        return render_template("puzzle.html", clue='Nope, Try again!'), 400
