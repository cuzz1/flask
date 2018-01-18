from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    name = StringField("what's you name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
