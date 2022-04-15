from flask import Flask, render_template

# Flask determines which of these methods to call based on the route accessed/ the decorator called.
app = Flask(__name__)

# app = Flask(__name__, template_folder='Days32-58:Intermediate+/day56')


# Execute hello_world() only if the user is trying to access the url homepage '/'
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/bye')
def say_bye():
    return "Bye"
	

if __name__=="__main__":
	app.run(debug=True)