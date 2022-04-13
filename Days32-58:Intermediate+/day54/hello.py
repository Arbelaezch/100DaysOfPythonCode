from flask import Flask

# Flask determines which of these methods to call based on the route accessed/ the decorator called.
app = Flask(__name__)


# Execute hello_world() only if the user is trying to access the url homepage '/'
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bye')
def say_bye():
    return "Bye"
	

if __name__=="__main__":
	app.run()