from flask import Flask
import time
import random

# Flask determines which of these methods to call based on the route accessed/ the decorator called.
app = Flask(__name__)

correct_num = random.randint(1, 10)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
    
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

def make_red(function):
    def wrapper():
        return '<style="color:red;">' + function()
    return wrapper
    

# Execute hello_world() only if the user is trying to access the url homepage '/'
@app.route("/")
@make_bold
@make_emphasis
def hello_world():
    return "<h1>Guess a number between 1 and 10</h1>"

@app.route('/<int:num>')
def decorator_function(num):
    if num < correct_num:
        return "<h1 style='color: red;'>Too Low</h1>"
    elif num > correct_num:
        return "<h1 style='color: red;'>Too High</h1>"
    else:
        return "<h1 style='color: green; text-align: center;''>Just Right</h1>" \
    			'<p>This is a paragraph</p>' \
				'<img style="width: 500px;" src="https://www.lomsnesvet.ca/wp-content/uploads/sites/21/2019/08/Kitten-Blog.jpg">'\
				'<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif">'



if __name__=="__main__":
    # Run the app in debug mode to reload the server automatically.
	app.run(debug=True)




# def delay_decorator(function):
# 	def wrapper_function():
# 		time.sleep(2)
# 		# Do something before function.
# 		function()
# 		# Do something after the function, or run the function multiple times.
# 	return wrapper_function

# @delay_decorator
# def say_hello():
#     print('Hello')

# @delay_decorator
# def say_bye():
#     print("bye")
 
# def say_greeting():
#     print("How are you?")

# say_hello()

# # Same result as the above @ methods, just different syntax.
# decorated_function = delay_decorator(say_greeting)
# decorated_function()