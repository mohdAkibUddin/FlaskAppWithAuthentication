from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired


class NewForm(FlaskForm):
    identifier = TextField(
        "ID",
        validators=[DataRequired()]
    )
    name = TextField(
        "Name",
        validators=[DataRequired()]
    )
    movie = TextField(
        "Movie",
        validators=[DataRequired()]
    )
    age = TextField(
        "Age",
        validators=[DataRequired()]
    )
    year = TextField(
        "Year",
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit")


