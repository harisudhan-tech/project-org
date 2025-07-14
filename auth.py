from flask import session, jsonify
import json, os

DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"users": [], "loans": []}, f)
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_current_user():
    if 'email' in session:
        data = load_data()
        for user in data['users']:
            if user['email'] == session['email']:
                return user
    return None

def login_user(email, password):
    data = load_data()
    for user in data['users']:
        if user['email'] == email and user['password'] == password:
            session['email'] = email
            return {"message": "Login successful", "role": user['role']}, 200
    return {"message": "Invalid credentials"}, 401

def logout_user():
    session.clear()
    return {"message": "Logged out"}, 200

def seed_users():
    data = load_data()
    if not data['users']:
        data['users'] = [
            {"id": "admin1", "email": "hari@admin", "password": "admin123", "role": "admin"},
            {"id": "cust1", "email": "john@customer", "password": "cust123", "role": "customer"}
        ]
        save_data(data)
