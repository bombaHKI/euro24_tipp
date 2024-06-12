# admin.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from functools import wraps
from secrets import token_urlsafe
import db
from sema import User, Candidate, Bet, Follow
from send_email import send_email

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin login required decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/')
@login_required
@admin_required
def index():
    return render_template('admin/admin_header.jinja')

@admin_bp.route('/users', methods=['GET', 'POST'])
@login_required
@admin_required
def users():
    if request.method == 'GET':
        candidates = Candidate.query.all()
        users = User.query.all()
        return render_template('admin/users.jinja',
                               candidates=candidates,
                               users=users)
    
    try:
        data = request.json
        action = data['action']
        user_data = data['userData']
        
        if not action or not user_data:
            return {"response": "Missing action or user data", "type": "error"}
        
        if action == 'addUser':
            return add_user(user_data)
        elif action == "delete-user":
            return delete_user(user_data)
        else:
            return handle_candidate(action, user_data["id"])

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return {"response": "Internal Server Error", "type": "error"}

def delete_user(user_data):
    id = user_data["id"]
    if not id:
        return {"response": "Nincs u_id!", "type": "error"}
    
    user = User.query.get(int(id))
    if not user:
        return {"response": "Ehhez az u_id-hoz nincs fiók!", "type": "error"}
    db.session.query(Follow).filter_by(whom_id=user.user_id).delete()
    db.session.query(Follow).filter_by(who_id=user.user_id).delete()
    Bet.query.filter_by(user_id=user.user_id).delete()
    db.session.delete(user)
    db.session.commit()
    return {"response": "Fiók törölve!", "type": "message"}

def add_user(user_data):
    password = token_urlsafe(13)
    if User.query.filter(User.email == user_data["email"]).first():
        return {"response": "Email cím már létezik!", "type": "error"}

    new_user = User(
        name=user_data["name"],
        email=user_data["email"]
    )
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    send_email(new_user, "at_new_user", password)
    return {"response": "Fiók létrehozva!", "type": "message"}

def handle_candidate(action, candidate_id):
    if not candidate_id:
        return {"response": "Missing candidate ID", "type": "error"}

    candidate = Candidate.query.get(int(candidate_id))
    if not candidate:
        return {"response": "Candidate not found", "type": "error"}
    
    if action == "accept-candidate":
        user = User(
            name=candidate.name,
            email=candidate.email
        )
        password = token_urlsafe(13)
        user.set_password(password)
        db.session.add(user)
        send_email(user, "at_new_user", password)
        message = "Jelentkező sikeresen hozzáadva!"
    elif action == "delete-candidate":
        message = "Jelentkező törölve!"
    else:
        return {"response": "Unknown action", "type": "error"}
    
    
    db.session.delete(candidate)
    db.session.commit()
    return {"response": message, "type": "message"}

@admin_bp.route('/meccsek', methods=['GET', 'POST'])
@login_required
@admin_required
def meccsek():
    if request.method == 'GET':
        return render_template('admin/add_meccsek.jinja')
    
    flash('User created successfully', 'success')
    return redirect(url_for('admin.admin_dashboard'))

