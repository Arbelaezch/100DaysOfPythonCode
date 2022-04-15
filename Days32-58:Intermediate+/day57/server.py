from flask import Flask, render_template
import random
import datetime
import requests

# Flask determines which of these methods to call based on the route accessed/ the decorator called.
app = Flask(__name__)

year = datetime.datetime.now().year

agify = requests.get("https://api.agify.io/")


# Execute hello_world() only if the user is trying to access the url homepage '/'
@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    return render_template("index.html", year=year)

@app.route('/<name>')
def say_bye(name):
	agify = requests.get(f"https://api.agify.io/?name={name}").json()
	genderfy = requests.get(f"https://api.genderize.io/?name={name}").json()

	return render_template("index.html", name=name.title(), gender=genderfy["gender"], age=agify["age"], year=year)

@app.route("/blog/<num>")
def get_blog(num):
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=blog_posts)
	

if __name__=="__main__":
	app.run(debug=True)