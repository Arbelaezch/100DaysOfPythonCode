from crypt import methods
import email
from wsgiref.validate import validator
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length, Email
import email_validator
from flask import Flask
from flask_bootstrap import Bootstrap


WTF_CSRF_SECRET_KEY = 'ioyubrfpiuadfspiub'


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=3)])
    submit = SubmitField(label='Log In')

# app = Flask(__name__)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	login_form = LoginForm()
	if login_form.validate_on_submit():
		if login_form.email.data == "admin@email.com" and login_form.password.data == "1234":
			return render_template('success.html', form=login_form)
		else:
			return render_template('denied.html', form=login_form)
	return render_template('login.html', form=login_form)




if __name__ == '__main__':
    app.run(debug=True)