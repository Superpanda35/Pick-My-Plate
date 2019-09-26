from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

class Form(FlaskForm):
    radiofield1=RadioField("Is meat fine?",
                           choices=[('yes','yes'),('no','no')])
    radiofield2=RadioField("Is dairy fine?",
                           choices=[('yes','yes'),('no','no')])
    radiofield3=RadioField("Is gluten fine?",
                           choices=[('yes','yes'),('no','no')])
    submit=SubmitField("submit")
