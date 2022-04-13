# Python Decorator Function

import time

	
def delay_decorator(function):
	def wrapper_function():
		time.sleep(2)
		# Do something before function.
		function()
		# Do something after the function, or run the function multiple times.
	return wrapper_function

@delay_decorator
def say_hello():
    print('Hello')

@delay_decorator
def say_bye():
    print("bye")
 
def say_greeting():
    print("How are you?")

say_hello()

# Same result as the above @ methods, just different syntax.
decorated_function = delay_decorator(say_greeting)
decorated_function()
    