# A Flask web app integrating SQLAlchemy that allows you to add your favorite
# films and display them. Allows you to change ratings, reviews, and update the
# list order.


from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form
from wtforms.validators import DataRequired
import requests
import json
from sqlalchemy import desc, asc
import sqlalchemy

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
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(1000), nullable=True)
    img_url = db.Column(db.String(1000), nullable=False)
    
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
MOVIE_ENDPOINT = "https://api.themoviedb.org/3/search/movie"


@app.route("/")
def home():
    rank = 1
    movie_list = Movie.query.order_by(desc(Movie.rating)).all()
    for movie in movie_list:
        movie.ranking = rank
        rank += 1
    
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
		response = requests.get(f"{MOVIE_ENDPOINT}?api_key={MOVIE_API_KEY}&query={form.title.data}")
  
		if response.status_code == 200:
			all_movies = json.loads(response.content.decode('utf-8'))	
			movie_list = []
			
			for movie in all_movies["results"]:
				movie_list.append(movie)	
			return render_template("select.html", all_movies=movie_list)
	
	return render_template("add.html", form=form)


@app.route("/edit")
def add_film():
	id = request.args.get('id')

	# For Search
	# https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
 
	response = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={MOVIE_API_KEY}&language=en-US")
	if response.status_code:
			movie = json.loads(response.content.decode('utf-8'))
			print(movie)

			img_path = f'https://image.tmdb.org/t/p/original{movie["poster_path"]}'

			movie = Movie(id=id, title=movie["title"], year=movie["release_date"][0:4], description=movie["overview"], rating=0, ranking=0, review="None", img_url=img_path)
			db.session.add(movie)
			db.session.commit()
	return redirect(url_for("update", id=id))



if __name__ == '__main__':
    app.run(debug=True)
