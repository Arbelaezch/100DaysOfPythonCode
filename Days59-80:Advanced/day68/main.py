from crypt import methods
import sqlite3
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




@app.route('/')
def home():
    if current_user.is_authenticated:
         return render_template("index.html", logged_in=True)
    else:
         return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		user = User.query.filter_by(email=request.form['email']).first()
		if user:
			error = 'Email already exists.'
			return render_template('register.html', error=error)
		else:
			# Werkzeug helper function for hashing + salting password
			password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
			
			user = User(name=request.form['name'], email=request.form['email'], password=password)
			db.session.add(user)
			db.session.commit()
			login_user(user)

			return redirect(url_for('secrets', user=user.name))
    
	return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
 
	if request.method == 'POST':
		password = request.form.get('password')
		try:
			user = User.query.filter_by(email=request.form['email']).first()
			if check_password_hash(user.password, password):
				login_user(user)
				flash('Logged in successfully.')

				return redirect(url_for('secrets', user=user.name))
			else:
				# Flask Flash messages
				error = 'Invalid credentials'
				return render_template('login.html', error=error)
		except:
				error = 'Email does not exist.'
				return render_template('login.html', error=error)
            
	return render_template('login.html')

@app.route('/secrets')
@login_required
def secrets():
    user = request.args['user']
    return render_template("secrets.html", user=user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf")






if __name__ == "__main__":
    app.run(debug=True)
