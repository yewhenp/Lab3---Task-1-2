"""
Module for web app generating a map of twitter user`s friendlist
"""

import urllib
from flask import Flask, render_template, request
import task3

app = Flask(__name__)

@app.route('/')
def index():
    """
    Index page function
    """
    return render_template('index.html')

@app.route("/generate", methods=["POST"])
def generate():
    """
    Map generation page function
    """
    try:
        task3.main(request.form.get("uname"), int(request.form.get("count")))
    except ValueError:
        return render_template("error.html")
    except urllib.error.HTTPError:
        return render_template("error.html")

    return render_template("Map_people.html")

app.run(debug=True)
