# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, sessions, session as loging_session
from databases import add_user_to_database, getallusers

from model import *
import os

# Starting the flask app
app = Flask(__name__)

# App routing code here
# @app.route('/home', methods=['GET','POST'])
app.config['SECRET_KEY'] = 'giladisking'

# Running the Flask app



@app.route('/')
def home():
    return render_template("the_website.html")



# sign up

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        name = request.form['name']
        password =request.form['password']
        mail= request.form['mail']
        users=getallusers()
        for user in users:
            if user.mail == mail:
                return render_template("signup.html", massage = "email already exist in the system")
        add_user_to_database(name,password, mail)        
        return render_template('the_website.html',email = mail)


# sign in

@app.route('/sign_in' , methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('signin.html')
    else: 
        mail= request.form['mail']
        password =request.form['password']
        users=getallusers()
        for user in users:
            if user.mail == mail and user.password==password:
                loging_session['mail'] = mail
                return render_template('the_website.html')
        return render_template("signin.html" , massage = "wrong email or password")



if __name__ == "__main__":
    app.run(debug=True)