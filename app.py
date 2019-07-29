# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, sessions, session as loging_session
from databases import *
import os
from flask_mail import Mail, Message
from model import *
# Starting the flask app
app = Flask(__name__)
mail=Mail(app)

# App routing code here
# @app.route('/home', methods=['GET','POST'])
app.config['SECRET_KEY'] = 'xGOWx'

# Running the Flask app

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":'GOWmeet@gmail.com',
    "MAIL_PASSWORD": 'meetGOW123'
}

app.config.update(mail_settings)
mail=Mail(app)

@app.route('/' , methods =['GET', 'POST'] )
def home():
    if request.method = 'get':
        return render_template("the_website.html")
    else:
        vol_email=request.form['email']
        Add_vol_mail(vol_email)
        render_template("the_website.html")


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



@app.route('/Apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'GET':
           return render_template('application_2.html')
    else:
        name = request.form['name']
        adress = request.form['adress']
        phone=request.form['phone']
        email=request.form['email']
        msg = Message("Hello ",
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients=["GOWmeet@gmail.com"])
        msg.body = "name: "+str(name) + "\n adress: "+ str(adress) +"\n mail: "+str(email) + "\nphone: "+str(phone) +"\n registered" 
        mail.send(msg)
        Add_Application(name, email, phone, adress)
        return redirect("/")

@app.route('/Apply_heb')
def apply_heb():
    if request.method == 'GET':
           return render_template('Apply_heb.html')
    else:
        name = request.form['name']
        adress = request.form['adress']
        phone=request.form['phone']
        email=request.form['email']
        msg = Message("Hello " + str(name),
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients="GOWmeet@gmail.com")
        msg.body = "name: "+str(name) + "\n adress: "+ str(adress) +"\n mail: "+str(email) + "\nphone: "+str(phone) +"\n registered" 
        mail.send(msg)
        Add_Application(name, email, phone, adress)
        return render_template('the_website.html')
 

@app.route('/Apply_arb')
def apply_arb():
    if request.method == 'GET':
           return render_template('Apply_arb.html')
    else:
        name = request.form['name']
        adress = request.form['adress']
        phone=request.form['phone']
        email=request.form['email']
        msg = Message("Hello" + name,
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients="GOWmeet@gmail.com")
        msg.body = "name: "+str(name) + "\n adress: "+ str(adress) +"\n mail: "+str(email) + "\nphone: "+str(phone) +"\n registered" 
        mail.send(msg)
        Add_Application(name, email, phone, adress)
        return render_template('the_website.html')
        


@app.route('/donate')
def donate():
    return render_template("donations.html")



@app.route('/H5T8N7')
def showmails():
    return render_template("showmails.html", mails = get_all_vol_mails())

  



if __name__ == "__main__":
    app.run(debug=True)
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

