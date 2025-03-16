from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, URLField, SelectField, TimeField
from wtforms.validators import DataRequired
import csv
import os
import dotenv

dotenv.load_dotenv()
FLA_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = "FLA_SECRET_KEY"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location (Google Map) URL', validators=[DataRequired()])
    open_time = TimeField('Open Time', validators=[DataRequired()], format='%H:%M')
    closing_time = TimeField('Closing Time', validators=[DataRequired()], format='%H:%M')
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired()], default = "0", choices=[("0", "✘")] + [(str(i),i*"☕️") for i in range(1,6)])
    wifi_rating = SelectField('WiFi Rating', validators=[DataRequired()], default = "0", choices=[("0", "✘")] +[(str(i),i*"💪") for i in range(1,6)])
    power_rating = SelectField('Power Outlet Rating', validators=[DataRequired()], default = "0", choices=[("0", "✘")] +[(str(i),i*"🔌") for i in range(1,6)])
    submit = SubmitField('Submit')
    
    def validate_location(self, field):
        if not field.data.startswith("http") or "www." not in field.data and ".com" not in field.data :
            raise ValidationError('URL must start with http')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("Coffee Wifi\cafe-data.csv","a", newline='', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            data = [form.cafe.data, form.location.data, form.open_time.data.strftime('%H:%M'), form.closing_time.data.strftime('%H:%M'), form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
            csv_data.writerow(data)
            return render_template('add.html', form=form, success=True)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open("Coffee Wifi\cafe-data.csv", newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)