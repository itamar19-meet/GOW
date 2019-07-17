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


@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        name = request.form['name']
        password =request.form['password']
        mail= request.form['mail']
        
        
        add_user_to_database(name,password, mail)        
        return render_template('response.html',email = mail)
@app.route('/sign_in' , methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    else: 
        mail= request.form['mail']
        password =request.form['password']
        users=getallusers()
        for user in users:
            if user.mail == mail and user.password==password:
                loging_session['name'] = name
                return render_template('homepage.html')

        if (loginflag==False):
            return render_template('signin', email = mail)



if __name__ == "__main__":
    app.run(debug=True)