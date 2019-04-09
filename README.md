# FindTheNextPage
Simple game where clues lead you from page to page.

![Welcome page](/resources/1_welcome.png)
![Page 1](/resources/2_page1.png)
![Page 2](/resources/3_page2.png)

# Requirements

NOTE: This has been written and tested for Python 3.6, but should work with newer versions.

This project requires [Flask]: https://pypi.org/project/Flask/

# Running the game

The game is built using flask.

```bash
user@computer ~/server $ python run.py
```

# Adding your own clues and pages

All clues and pages are stored in a Dictionary in the views.py file in the App directory.

```python
#Dictionary for storing pages and clues

# Individually defined keys
pages['1'] = '1'        #Arabic numerals
pages['2'] = '10'       #Binary
pages['11'] = 'IV'      #Roman numerals
pages['V'] = 'evif'     #Number written backwards (english)
pages['xis'] = 'Nice!'  #The end / Congratulations

# or as a
# Single declaration
pages ={'1': '1', \ 
        '2': '10', \
        '11': 'IV',\
        'V': 'evif',\
        'xis': 'Nice!'}

```
You can add as many pages as you would like, as long as the page names / URLs are unique.
