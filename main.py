from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from add_cafe_form import CafeForm

app = Flask(__name__)
# The secret key is needed to keep the client-side sessions secure.
app.config['SECRET_KEY'] = 'any_string_you_want'  
app.debug = True
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            print(type(f"LOCATION TYPE: {form.cafe_location.data}"))
            csv_file.write(f"\n{form.cafe_name.data},"
                    f"{form.cafe_location.data.replace(',', '')},"
                    f"{form.opening_time.data},"
                    f"{form.closing_time.data},"
                    f"{form.coffee_rating.data},"
                    f"{form.wifi_rating.data},"
                    f"{form.power_rating.data}")
            return redirect('cafes')
    return render_template('add.html', form=form)

@app.route('/cafes') 
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run()