# FindTheNextPage
Simple game where clues lead you from page to page.

![Welcome page](/resources/1_welcome.png)
![Page 1](/resources/2_page1.png)
![Page 2](/resources/3_page2.png)

# Running the game

The game is built using flask.

```bash
user@computer ~/server $ python run.py
```

# Adding your own clues and pages

All clues and pages are stored in a Dictionary in the views.py file in the App directory.

```python
#Dictionary for storing pages and clues

pages ={'1': '1', \
        '2': '10', \
        '11': 'IV',\
        'V': 'evif',\
        'xis': 'Nice!',
```
You can add as many pages as you would like, as long as the page names / URLs are unique.
