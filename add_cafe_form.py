from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', [DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps', [DataRequired(), URL(require_tld=True, message="Invalid URL")])
    opening_time = StringField('Opening Time e.g. 8AM', [DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', [DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')