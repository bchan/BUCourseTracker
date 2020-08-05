import time
from flask import Flask, request, Response
import json

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/signIn', methods=['POST'])
def signin_handler():
    email = request.args.get('email')
    password = request.args.get('password')
    data = {'email': email, 'password': password}

    if email is None:
        return 'No email submitted.', 400

    if password is None:
        return 'No password submitted.', 400

    if check_account_exists(email):
        return data, 200
    else:
        return 'Account does not exist', 400


@app.route('/api/signUp', methods=['POST'])
def signup_handler():
    email = request.args.get('email')
    password = request.args.get('password')
    data = {'email': email, 'password': password}

    if email is None:
        return 'No email submitted.', 400

    if password is None:
        return 'No password submitted.', 400

    if check_account_exists(email):
        return 'Account already exists!', 400

    return data, 200





'''
FUNCTIONS TO PUT INTO A MODULE
'''



# Checks if a user account exists
def check_account_exists(email):
    all_accounts = read_accounts()

    for account in all_accounts:
        if email == account['email']:
            return True

    return False


# Creates a new account if one doesn't exist already
def create_account():
    print("CREATING ACCOUNT")
    read_accounts()
    return


def read_accounts():
    accounts = []
    with open('./json_files/account_db') as json_file:
        data = json.load(json_file)
        for i in data['accounts']:
            accounts.append(i)
            # print('First Name: ' + account['firstName'])
            # print('Last Name: ' + account['lastName'])
            # print('Email: ' + account['email'])
            # print('Password: ' + account['password'])
            # print('')

    return accounts
