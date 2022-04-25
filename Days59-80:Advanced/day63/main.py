from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form
from wtforms.validators import DataRequired
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


# Create Table 
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(100), nullable=False)
    
    # Allows each book object to be identified by its title when printed.
    def __repr__(self):
        return '<Movie %r>' % self.title

# SQLITE USING SQLALCHEMY
db.create_all()

# Update Form for ratings
class UpdateForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10. e.g. 6', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

# Add movie form
class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')
    
MOVIE_API_KEY = "aaa5b990b039682b1209b8c632abb25e"
MOVIE_ENDPOINT = "https://api.themoviedb.org/3/search/movie?"


@app.route("/")
def home():
    movie_list = Movie.query.all()
    return render_template("index.html", all_movies=movie_list)

@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
	form = UpdateForm(request.form)
	movie_obj = Movie.query.get(id)
	if request.method == 'POST' and form.validate():
		movie_obj.rating = form.rating.data
		movie_obj.review = form.review.data
		db.session.commit()
		return redirect(url_for("home"))
	return render_template("edit.html", movie=movie_obj, form=form)

@app.route("/delete")
def delete():
	movie_id = request.args.get('id')
	movie_to_delete = Movie.query.get(movie_id)
	db.session.delete(movie_to_delete)
	db.session.commit()
	return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
	form = AddForm()
	if request.method == "POST":
		# movie = Movie(title=request.form["title"], year=request.form["year"], description=request.form["description"], rating=request.form["rating"], ranking=request.form["ranking"], review=request.form["review"], img_url=request.form["img_url"])
		query = {
			"query": form.title.data
		}
		response = requests.get(f"{MOVIE_ENDPOINT}api_key={MOVIE_API_KEY}&query={form.title.data}")
		# movie = response.json
		if response.status_code == 200:
			# movie = json.loads(response.content.decode('utf-8'))
			# movie_entry = Movie(title=movie["results"][1]["title"], year=movie["results"][1]["release_date"][0:4], description=movie["results"][1]["overview"], rating=request.form["rating"], ranking=request.form["ranking"], review=request.form["review"], img_url=request.form["img_url"])
			# db.session.add(movie_entry)
			# db.session.commit()
			movie = json.loads(response.content.decode('utf-8'))

			return redirect(url_for("select", movie=movie))

	return render_template("add.html", form=form)

@app.route("/select")
def select():
	movie = request.args.get('movie')
	movie = json.dumps(movie)
    
	# movie_list = request.args.get('movie_list')
	return render_template("select.html", all_movies=movie)


if __name__ == '__main__':
    app.run(debug=True)
