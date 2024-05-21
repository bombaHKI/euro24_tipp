from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
import json
import os
from sema import User, Candidate
from db import session

def create_app():
   config = json.load(open(os.path.join(os.path.dirname(__file__), 'data/config.json'), 'r', encoding='utf-8'))
   app = Flask(__name__)
   app.config["SECRET_KEY"] = config["SECRET_KEY"]

   login_manager = LoginManager()
   login_manager.login_view = "login"
   login_manager.init_app(app)

   @login_manager.user_loader
   def load_user(user_id):
      # since the user_id is just the primary key of our user table, use it in the query for the user
      return User.query.get(int(user_id))

   return app
app = create_app()

@app.route("/")
def index():
   return render_template("alap.jinja")

@app.route("/login", methods=["GET","POST"])
def login():
   if request.method == "GET":
      return render_template("login.jinja")

   #TODO: SZERVER OLDALI TESZTEK: EMAIL HELYES-E (REGEX) FELHASZNÁLÓNÉV SPACE STB.
   error = None
   message = None
   formJSON = request.json
   email = formJSON["email"]
   if formJSON["action"] == "login":
      user = User.query.filter(User.email == email).first()
      if user == None or \
         not check_password_hash(user.password_hash, formJSON["password"]):
         error = "Jelszó vagy email nem stimmelt!"
      else:
         login_user(user)
   elif formJSON["action"] == "signup":
      name =  formJSON["username"]
      if User.query.filter(User.email == email).first() != None:
         error = "Ezzel az e-amil címmel már létezik fiók!"
      elif Candidate.query.filter(Candidate.email == email).first() != None:
         error = "Ezzel az e-amil címmel már jelentkeztek!"
      else:
         session.add(Candidate(name=name,
                              email=email))
         session.commit()
         message = "Sikeres jelentkezés!"
   if error != None:
      return {"response": error, "type": "error"}
   else:
      return {"response": message, "type": "message"}

if __name__ == "__main__":
   app.run(debug=True)
