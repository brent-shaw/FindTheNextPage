from flask import render_template
from app import app

pages ={'1': '1', \
        '2': '2', \
        '3': '3',\
        '4': '4',\
        '5': '5',}

@app.route('/')
def start():
    return render_template("index.html", clue="Welcome!")

@app.route('/<T>')
def p01(T):
    try:
        return render_template("puzzle.html", clue=pages[T])
    except:
        return render_template("puzzle.html", clue='Nope, Try again!')
