#                                                             God Bless U
# import libraries                                     
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired

# Instantiate Flask app
app = Flask( __name__ )

# Create a index route
@app.route("/")
def index():
    return render_template("hello/index.html")


