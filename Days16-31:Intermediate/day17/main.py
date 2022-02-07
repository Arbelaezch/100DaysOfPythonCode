import os

def screen_clear():
	'''Clears terminal screen'''
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		# for windows platfrom
		_ = os.system('cls')

class User:
	
	def __init__(self, user_id, username):
		#called every time a new User object is created.
		self.id = user_id
		self.username = username
		pass
	

screen_clear()

user_1 = User("001", "Jack")


print(user_1.username)