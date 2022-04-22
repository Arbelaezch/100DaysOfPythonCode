from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Time (e.g.8AM)', validators=[DataRequired()])
    close = StringField(label='Closing Time (e.g.8AM)', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=[("☕"), ("☕☕"), ("☕☕☕"),("☕☕☕☕"), ("☕☕☕☕☕")], validators=[DataRequired()])
    wifi = SelectField(label='Wifi Strength Rating', choices=[("💪"), ("💪💪"), ("💪💪💪"),("💪💪💪💪"), ("💪💪💪💪💪")], validators=[DataRequired()])
    power = SelectField(label='Power Rating', choices=[("🔌"), ("🔌🔌"), ("🔌🔌🔌"),("🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
	form = CafeForm()
	if form.validate_on_submit():
		newRow = [form.cafe.data,form.location.data,form.open.data,form.close.data,form.coffee.data,form.wifi.data,form.power.data]
		
		with open('Days59-80:Advanced/day61/cafe-data.csv', 'a+', newline='') as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow(newRow)
			
		return render_template('index.html', form=form)

	return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # cafe = url_for('cafe-data')
    with open('Days59-80:Advanced/day61/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
