# app.py
from flask import Flask,jsonfy ,render_template    # import flask

app = Flask(__name__)             # create an app instance
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/")                   # at the end point /
def index():                      # call method hello
    return jsonfy(books)#render_template("index.html")


         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run()
