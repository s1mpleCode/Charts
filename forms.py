from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

MONTH_LIST = [('01', 'January'),
              ('02', 'February'),
              ('03', 'March'),
              ('04', 'April'),
              ('05', 'May'),
              ('06', 'June'),
              ('07', 'July'),
              ('08', 'August'),
              ('09', 'September'),
              ('10', 'October'),
              ('11', 'November'),
              ('12', 'December'),
              ]


class MonthFilterForm(FlaskForm):
    month = SelectField('Type', choices=MONTH_LIST, validators=[DataRequired()])
    submit = SubmitField("Apply")
