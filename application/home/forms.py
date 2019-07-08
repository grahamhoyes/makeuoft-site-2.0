from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class MailingListForm(FlaskForm):
    """
    Registration that allows customers to register with their first name,
    last name, email and a password
    """
    email = StringField("Email", validators=[DataRequired(), Email()])
