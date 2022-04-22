from crypt import methods
from flask import Flask, render_template
import requests
from flask import request
import smtplib

my_email = "christian.arbelaez2@gmail.com"
password = "\F*r6MD6be,qFSQ^"


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

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=['POST'])
def receive_data():
    name = request.form["fname"]
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    
    # Connect to your email.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=email,
            to_addrs="arbelaezch@gmail.com",
            msg=f"\n\nFrom: {name}\n\n{message}\n\nPhone: {phone}\n\nEmail: {email}"
        )
    
    return "<h1>Successfully sent your message!</h1>"
    
    

if __name__ == "__main__":
    app.run(debug=True)