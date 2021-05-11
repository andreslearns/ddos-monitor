from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, IPAddress, ValidationError
from incapsula.sparc_api import get_imperva_api

choice_task =  open('data/divert_task.txt').read().splitlines()
choice_allowed_ip = open('data/allowed_network.txt').read().splitlines()

class DivertForm(FlaskForm):
    network = SelectField('Network', choices=choice_allowed_ip, validators=[DataRequired()],default=get_imperva_api()[0])
    task =  SelectField('Task',choices=choice_task, validators=[DataRequired()],default=choice_task[0])
    submit = SubmitField('Mitigate')