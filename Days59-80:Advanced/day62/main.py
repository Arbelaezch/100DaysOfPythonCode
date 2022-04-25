from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemy Create db
db = SQLAlchemy(app)

# Create Table 
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    # Allows each book object to be identified by its title when printed.
    def __repr__(self):
        return '<Book %r>' % self.title


# SQLITE USING SQLALCHEMY

db.create_all()
# admin = User(username='admin', email='admin@example.com')
# db.session.add(admin)
# db.session.commit()



# all_books = []

# SQLITE USING SQL
# # Create a connection to a new db at given location.
# db = sqlite3.connect("Days59-80:Advanced/day62/books-collection.db")
# # Create a cursor that controls the db.
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
	if request.method == "POST":
        # Using list
        # book = {
		# 	"title": request.form["title"],
		# 	"author": request.form["author"],
		# 	"rating": request.form["rating"]
		# }
        # all_books.append(book)
        
		book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
		db.session.add(book)
		db.session.commit()
        
		return redirect(url_for("home"))

	return render_template("add.html")


@app.route('/edit/<id>', methods=["GET", "POST"])
def change_rating(id):
	if request.method == "POST":
        # Update A Record By PRIMARY KEY
		# book_id = 1
		book_to_update = Book.query.get(id)
		book_to_update.rating = request.form["new_rating"]
		db.session.commit() 
  
		return redirect(url_for("home"))

	book_id = request.args.get('id', None)
	book_obj = Book.query.get(id)
	return render_template("edit.html", book=book_obj)

@app.route('/delete')
def delete():
	book_id = request.args.get('id')
	book_to_delete = Book.query.get(book_id)
	db.session.delete(book_to_delete)
	db.session.commit()
    
	return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug=True)

