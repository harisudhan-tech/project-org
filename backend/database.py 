import os
import json

DATA_FILE = 'data.json'

def load_data():
    """Load JSON data from file or create a default structure."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"users": [], "loans": []}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    """Save JSON data back to file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_users():
    return load_data().get("users", [])

def get_loans():
    return load_data().get("loans", [])

def set_users(users):
    data = load_data()
    data["users"] = users
    save_data(data)

def set_loans(loans):
    data = load_data()
    data["loans"] = loans
    save_data(data)
