# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, sessio
from databases import add_user, get_all_msgs, get_user_by_name, check_password, add_message, get_all_users, add_contact, add_pos
from model import *
# Starting the flask app
app = Flask(__name__)

# App routing code here
# @app.route('/home', methods=['GET','POST'])

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

