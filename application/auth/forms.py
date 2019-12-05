from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    DateField,
    SelectField,
    TextAreaField,
)
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from application.db_models import Users


class LoginForm(FlaskForm):
    email = StringField("E-Mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    """
    Registration that allows customers to register with their first name,
    last name, email and a password
    """

    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    submit = SubmitField("Register")

    def validate_email(self, email):
        search_email = Users.query.filter_by(email=email.data).first()
        if search_email is not None:
            raise ValidationError("Please use a different email address.")


class ApplicationForm(FlaskForm):
    """
    Application form that takes all of the information of contestants
    and puts it into the database
    """

    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    birthday = DateField("Birthday", validators=[DataRequired()])
    gender = SelectField(
        "Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    )
    ethnicity = StringField("Ethnicity", validators=[DataRequired()])

    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])

    school = StringField("School", validators=[DataRequired()])
    program = StringField("Program", validators=[DataRequired()])
    grad_year = StringField("Graduation Year", validators=[DataRequired()])

    resume = StringField("Resume Temp")

    q1_prev_hackathon = TextAreaField("Previous Hackathon", validators=[DataRequired()])
    q2_why_participate = TextAreaField("Why Participate", validators=[DataRequired()])
    q3_hardware_exp = TextAreaField("Hardware Experience", validators=[DataRequired()])

    how_you_hear = TextAreaField("How You Hear", validators=[DataRequired()])

    submit = SubmitField("Register")

    def validate_email(self, email):
        search_email = Users.query.filter_by(email=email.data).first()
        if search_email is not None:
            raise ValidationError("Please use a different email address.")


class ForgotPasswordEmailForm(FlaskForm):
    """
    Form takes email of contestant when they forgot their password
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
