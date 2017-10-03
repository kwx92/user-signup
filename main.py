from flask import Flask, request, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

form = """ 

"""
@app.route("/")
def index():
    return render_template('homepage.html')

def is_user(username):
    if ' ' in username:
        return False
    elif len(username) < 3 or len(username) > 20:
        return False
    else:
        username = request.form['username']
        return True
def is_password(password, v_password):
    if ' ' in password:
        return False
    elif len(password) < 3 or len(password) > 20:
        return False
    elif password != v_password:
        return False
    else:
        return True

def is_email(email):
    if email == '':
        return True
    elif '@' not in email and '.' not in email:
        return False
    else:
        return True

@app.route('/', methods=['POST'])
def login():
    password = request.form['password']
    v_password = request.form['v_password']
    username = request.form['username']
    email = request.form['email']
    p_error = ''
    user_error = ''
    email_error = ''
    login = False
    if not is_user(username):
        user_error = 'Please make sure username is 3-20 characters, and does not contain spaces'
        login = False
    if not is_password(password, v_password):
        p_error = 'Please make sure passwords match, are 3-20 characters, and do not contain spaces'
        login = False
    if not is_email(email):
        email_error = 'Please be sure email is formatted properly with @ and . characters'
        login = False
    if not user_error and not p_error and not email_error:
        login = True
    if not login:
        return render_template('homepage.html', user_error=user_error, username=username, p_error=p_error, email_error=email_error, email=email)
    else:
        return '<p>Hello {0}, your login was successful!</p>'.format(username)
    
app.run()