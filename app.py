# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, sessions, session as loging_session

import os

# Starting the flask app
app = Flask(__name__)

# App routing code here
# @app.route('/home', methods=['GET','POST'])
app.config['SECRET_KEY'] = 'xGOWx'

# Running the Flask app



@app.route('/')
def home():
    return render_template("the_website.html")

@app.route('/hebrew')
def hebrew_web():
    return render_template("hebrew_website.html")


@app.route('/arabic')
def arabic_web():
    return render_template("arabic_website.html")


@app.route('/team')
def team():
    return render_template("teams.html")

@app.route('/level')
def level():
    return render_template("levels.html")



@app.route('/Apply')
def apply():
    return render_template("Apply.html")

@app.route('/Apply_heb')
def apply_heb():
    return render_template("Apply_heb.html")


@app.route('/Apply_arb')
def apply_arb():
    return render_template("/Apply_arb.html")

# # sign up
# mail_holder = ""
# name_holder = ""
# massage_holder =""




# @app.route('/sign_in' , methods=['GET', 'POST'])
# def sign_in():
#     if request.method == 'GET':
#         return render_template('signin.html')
#     else: 
#         mail= request.form['mail']
#         password =request.form['password']
#         users=getallusers()
#         for user in users:
#             if user.mail == mail and user.password==password:
#                 loging_session['mail'] = mail
#                 mail_holder = mail
#                 name_holder = name
#                 return redirect('/logged')
#         return render_template("signin.html" , massage= "wrong email or password")

# @app.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'GET':
#         return render_template('signup.html')
#     else:
#         name = request.form['name']
#         password =request.form['password']
#         mail= request.form['mail']
#         mail_holder = mail
#         name_holder = name
#         users=getallusers()
#         for user in users:
#             if user.mail == mail:
#                 return render_template("signup.html" , massage = "email already exist in the system")
#         add_user_to_database(name,password, mail)        
#         return redirect('/logged')


# @app.route('/logged' , methods=['GET', 'POST'])
# def logged_in():

#         return render_template('the_website.html' , name = name_holder , mail =mail_holder)

if __name__ == "__main__":
    app.run(debug=True)