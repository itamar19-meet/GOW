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
        idnum = request.form['idnum']
        password =request.form['password']
        mail= request.form['mail']
        users=getallusers()
        nameflag=False
        idflag=False
        mailflag=False
        for u in users:
            if u.name==name:
                return render_template('signup.html', nameflag=nameflag)
            if u.idnum==idnum:
                return render_template('signup.html', idflag=idflag)
            if u.mail==mail:
                return render_template('signup.html', mailflag=mailflag)


        add_user_to_database(name, idnum, password, mail)        
        return render_template('response.html',
            n=name
            )
@app.route('/sign_in' , methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        idnum = request.form['idnum']
        password =request.form['password']
        loginflag=False
        users=getallusers()
        for user in users:
            if user.idnum==idnum and user.password==password:
                loginflag=True
                loging_session['name'] = name
                return render_template('homepage.html')

        if (loginflag==False):
            return render_template('signin', loginflag=loginflag)



if __name__ == "__main__":
    app.run(debug=True)