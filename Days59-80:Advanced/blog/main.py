from crypt import methods
from datetime import date
from distutils.debug import DEBUG
import requests
import email
from email.message import EmailMessage
from flask import Flask, flash, render_template, redirect, request, url_for, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Email
from wtforms.widgets import PasswordInput
from flask_ckeditor import CKEditor, CKEditorField
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from functools import wraps
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)



##CONFIGURE DB TABLES
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    
    #This will act like a List of BlogPost objects attached to each User. 
    #The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")
    

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
    #Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    #Create reference to the User object, the "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")
    
    comments = relationship("Comment", back_populates="parent_post")
    
    
class Comment(db.Model, UserMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    blog_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    

# db.create_all()



##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
 
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", widget=PasswordInput(hide_value=False), validators=[DataRequired()])   
    submit = SubmitField("Submit Post")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", widget=PasswordInput(hide_value=False), validators=[DataRequired()])   
    submit = SubmitField("Submit Post")
    
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Admin only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)        
    return decorated_function



@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	error = None
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		
		if user:
			if user.password == form.password.data:
				login_user(user)
		
				
				return redirect('/')
			else:
				return render_template('login.html', form=form, error='Incorrect credentials.')
		else:
			return render_template('login.html', form=form, error='The email does not exist.')
	return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		new_user = User(name=form.name.data, email=form.email.data, password=form.password.data)
  
		db.session.add(new_user)
		db.session.commit()
		return redirect('/')
	return render_template('register.html', form=form)


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    if current_user.is_authenticated:
         return render_template("index.html", all_posts=posts, logged_in=True)
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>", methods=['GET', 'POST'])
def show_post(index):
	posts = BlogPost.query.all()
	form = CommentForm()
	requested_post = None
	for blog_post in posts:
		if blog_post.id == index:
			requested_post = blog_post
			comments = blog_post.comments
	if form.validate_on_submit():
		if not current_user.is_authenticated:
			flash("You need to login or register to comment.")
			return redirect(url_for("login"))

		new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )

		db.session.add(new_comment)
		db.session.commit()
		form.comment_text.data = ''
	
            
	return render_template("post.html", post=requested_post, form=form, comments=comments)




@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
	posts = BlogPost.query.all()
	requested_post = None
	for blog_post in posts:
		if blog_post.id == post_id:
			post = blog_post
	form = CreatePostForm(title=post.title, subtitle=post.subtitle, img_url=post.img_url, author=post.author, body=post.body)
	if form.validate_on_submit():
		post.title=form.title.data
		post.subtitle=form.subtitle.data
		post.author=form.author.data
		post.img_url=form.img_url.data
		post.body=form.body.data
  
		db.session.commit()
		return redirect('/')
    
	return render_template("make-post.html", form=form, post=post)

@app.route("/new-post", methods=['GET', 'POST'])
@admin_only
def new_post():
	user = User.query.filter_by(email=current_user.email).first()
	form = CreatePostForm()
	if form.validate_on_submit():
		current_date = date.today()
		current_date = current_date.strftime("%B %d, %Y")
		
		new_post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, author=user, img_url=form.img_url.data, body=form.body.data, date=current_date)
  
		db.session.add(new_post)
		db.session.commit()
		return redirect('/')
	return render_template("make-post.html", form=form)

@app.route("/delete/<post_id>")
@admin_only
def delete_post(post_id):
	post = BlogPost.query.get(post_id)
	db.session.delete(post)
	db.session.commit()
    
	return redirect('/')


@app.route("/about")
def about():
    if current_user.is_authenticated:
         return render_template("about.html")
    return render_template("about.html")


@app.route("/contact")
def contact():
    if current_user.is_authenticated:
         return render_template("contact.html")
    return render_template("contact.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)