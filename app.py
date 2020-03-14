# app.py
from flask import Flask,jsonify ,render_template    # import flask

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def index():                      # call method hello
    return render_template("index.html")

@app.route("/photo")                   # at the end point /
def photo():                      # call method hello
    return render_template("photo.html")

         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run()
