"""
Hazel's explanation and demo code of CORS from the lab
======================================================

Cross-Origin
CORS: 

Let's imagine you have two websites:

1. Zoe's Happy Fun Online Discussion Emporium
2. Hazel's Evil Discussion Ruining Hacker Troll Site

On website 1, we have a FORM that does a POST to make a post on the discussion
On website 2 (the evil website), all we have to do is tell the browser to make
a POST to the same URL on website as the FORM would POST to... except, we can
fill it in with our own NEFARIOUS AND EVIL CONTENT!!!

If the user for example, is logged into website 1, but they also browse to
website 2, the website 2 can make their browser post FOR THEM to website 1,
and it can make them say WHATEVER THEY WANT!!!

"""

fancy_html= """
<!doctype html>
<html>
<head>
</head>
<body>
<h1 style="color: #ff00ff;">Fancy TODO List!</h1>
<ol>
TODOITEMS
</ol>
</body>
</html>
"""

# XSS ATTACK EXAMPLE

from flask import escape #XSS

@app.route("/fancy")
def hello():
    # do curl thing
    # instead - wrap task in escape(task['task']) >> changes it to just text in the HTML
    todo_items = [f"<li>{task['task']}</li>" for number, task in TODOs.items()]
    return fancy_html.replace('TODOITEMS', '\n'.join(todo_items))