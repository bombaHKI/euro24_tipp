from flask import Flask, request, render_template, redirect, url_for
import json
import os

def create_app():
    config = json.load(open(os.path.join(os.path.dirname(__file__), 'data/config.json'), 'r', encoding='utf-8'))
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config["SECRET_KEY"]
    return app
app = create_app()

@app.route("/")
def index():
   return render_template("alap.jinja")

@app.route("/login", methods=["GET","POST"])
def login():
   if request.method == "GET":
      return render_template("login.jinja")

if __name__ == "__main__":
   app.run(debug=True)
