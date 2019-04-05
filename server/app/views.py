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
#Function for displaying the start page

@app.route('/')
def start():
    return render_template("index.html")

#------------------------------------------------------------------------------
#Function for returning each clue page / puzzle page
#Takes the page name and looks up clue in Pages Dictionary

@app.route('/<T>')
def puzzle(T):
    try:
        n = pages[T]
        return render_template("puzzle.html", number=n, clue=pages[T])
    except:
        return render_template("puzzle.html", clue='Nope, Try again!'), 400
