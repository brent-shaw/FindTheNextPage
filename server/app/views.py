from flask import render_template
from app import app

#------------------------------------------------------------------------------
#Dictionary for storing pages and clues
#
#Pages are in the forms of: '<address>': '<clue>'
#An example: {'1': 'Change the URL to page "2" ', \
#	      '2': 'Try speeling the next one out', \
#	      'three': 'That's it!'}

pages ={'1': '1', \
        '2': '2', \
        '3': '3',\
        '4': '4',\
        '5': '5',}

#------------------------------------------------------------------------------
#Function for displaying the start page

@app.route('/')
def start():
    return render_template("index.html", clue="Welcome!")

#------------------------------------------------------------------------------
#Function for returning each clue page / puzzle page
#Takes the page name and looks up clue in Pages Dictionary

@app.route('/<T>')
def puzzle(T):
    try:
        return render_template("puzzle.html", clue=pages[T])
    except:
        return render_template("puzzle.html", clue='Nope, Try again!')

#------------------------------------------------------------------------------
