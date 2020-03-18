# app.py
from flask import Flask,jsonify ,render_template, url_for    # import flask

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def index():                      # call method hello
    return render_template("index.html")

@app.route("/photo")                   # at the end point /
def photo():                      # call method hello
    return render_template("photo.html")

@app.route("/video")                   # at the end point /
def video():                      # call method hello
    return render_template("video.html")

@app.route("/webcam")                   # at the end point /
def webcam():                      # call method hello
    return render_template("webcam.html")


         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run()
