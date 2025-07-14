from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"users": [], "loans": []}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_user_by_email(email):
    data = load_data()
    return next((u for u in data['users'] if u['email'] == email), None)

@app.route('/api/login', methods=['POST'])
def login():
    creds = request.json
    user = get_user_by_email(creds['email'])
    if user and user['password'] == creds['password']:
        return jsonify({ "message": "Login successful", "role": user['role'], "email": user['email'] })
    return jsonify({ "message": "Invalid credentials" }), 401

@app.route('/api/loans', methods=['GET'])
def get_loans():
    email = request.args.get('email')
    user = get_user_by_email(email)
    if not user:
        return jsonify({ "message": "Unauthorized" }), 403

    data = load_data()
    if user['role'] == 'admin':
        return jsonify(data['loans'])
    else:
        user_loans = [loan for loan in data['loans'] if loan['customer_id'] == user['id']]
        return jsonify(user_loans)

@app.route('/api/loans', methods=['POST'])
def add_or_update_loan():
    loan = request.json
    email = loan.get('email')
    user = get_user_by_email(email)
    if not user or user['role'] != 'admin':
        return jsonify({ "message": "Unauthorized" }), 403

    data = load_data()

    # Check if loan_id exists, then update it
    for i, existing_loan in enumerate(data['loans']):
        if existing_loan['loan_id'] == loan['loan_id']:
            data['loans'][i] = loan
            save_data(data)
            return jsonify({ "message": "Loan updated" })

    # Otherwise, add new loan
    data['loans'].append(loan)
    save_data(data)
    return jsonify({ "message": "Loan added" })


@app.route('/api/loans/<loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    email = request.args.get('email')
    user = get_user_by_email(email)
    if not user or user['role'] != 'admin':
        return jsonify({ "message": "Unauthorized" }), 403

    data = load_data()
    data['loans'] = [loan for loan in data['loans'] if loan['loan_id'] != loan_id]
    save_data(data)
    return jsonify({ "message": "Loan deleted" })

@app.before_request
def seed_users():
    data = load_data()
    if not data['users']:
        data['users'] = [
            {"id": "admin1", "email": "hari@admin", "password": "admin123", "role": "admin"},
            {"id": "cust1", "email": "john@customer", "password": "cust123", "role": "customer"},,{
      "id": "cust2",
      "email": "hari@customer",
      "password": "cust123",
      "role": "customer"
    },{
      "id": "cust3",
      "email": "ragavan@customer",
      "password": "cust123",
      "role": "customer"
    }
        ]
        save_data(data)

if __name__ == '__main__':
    app.run(debug=True)
