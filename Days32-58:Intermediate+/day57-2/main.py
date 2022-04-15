from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=blog_posts)

@app.route("/post/<int:num>")
def get_post(num):
    num -= 1
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", post=blog_posts[num])

if __name__ == "__main__":
    app.run(debug=True)
