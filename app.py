from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sema import User, Candidate
from db import session
from send_email import send_email
from config import appConfigJson
from admin import admin_bp

def create_app():
   app = Flask(__name__)
   app.config["SECRET_KEY"] = appConfigJson["SECRET_KEY"]

   login_manager = LoginManager()
   login_manager.login_view = "login"
   login_manager.init_app(app)

   app.register_blueprint(admin_bp)

   @login_manager.user_loader
   def load_user(user_id):
      return User.query.get(int(user_id))

   return app
app = create_app()

@app.route("/")
@login_required
def index():
   return render_template("alap_header.jinja")

@app.route("/login", methods=["GET","POST"])
def login():
   if request.method == "GET":
      return render_template("login.jinja")

   error = None
   message = None
   formJSON = request.json
   email = formJSON["email"].strip()
   if formJSON["action"] == "login":
      user = User.query.filter(User.email == email).first()
      if user == None or \
         not user.check_password(formJSON["password"]):
         error = "Jelszó vagy email nem stimmelt!"
      else:
         login_user(user)
   elif formJSON["action"] == "signup":
      name =  formJSON["username"].strip()
      if User.query.filter(User.email == email).first() != None:
         error = "Ezzel az e-amil címmel már létezik fiók!"
      elif Candidate.query.filter(Candidate.email == email).first() != None:
         error = "Ezzel az e-amil címmel már jelentkeztek!"
      else:
         candidate = Candidate(name=name, email=email)
         session.add(candidate)
         session.commit()
         message = "Sikeres jelentkezés!"
         send_email(candidate,"at_signup")
   if error != None:
      return {"response": error, "type": "error"}
   else:
      return {"response": message, "type": "message"}

@app.route("/szabalyok")
@login_required
def szabalyok():
   return render_template("szabalyok.jinja")

@app.route("/meccsek")
@login_required
def meccsek():
   return render_template("alap_header.jinja")

@app.route("/allas", methods=["GET","POST"])
@login_required
def allas():
   return render_template("alap_header.jinja")

@app.route("/profil", methods=["GET","POST"])
@login_required
def profil():
   if request.method == "GET":
      return render_template("profil.jinja")

   error = None
   formJSON = request.json
   password = formJSON["password"]
   if not current_user.check_password(password):
      error = "Rossz jelszó!"
   elif formJSON["action"] == "data-change":
      current_user.name = formJSON["username"].strip()
      current_user.email =  formJSON["email"].strip()
      
   elif formJSON["action"] == "password-change":
      newPass =  formJSON["new-password"]
      confPass = formJSON["confirm-password"]
      if newPass != confPass:
         error = "Jelszó megerősítése nem egyezik!"
      else:
         current_user.set_password(newPass)

   if error == None:
      try:
         session.commit()
         send_email(current_user,"at_data_change")
         return {"response": "Sikeres módosítás!", "type": "message"}
      except:
         error = "Valami hiba történt!"
   return {"response": error, "type": "error"}

@app.route("/logout")
def logout():
   logout_user()
   return redirect(url_for("login"))

if __name__ == "__main__":
   app.run(debug=True)
