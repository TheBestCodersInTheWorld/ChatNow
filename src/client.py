from __future__ import print_function 
import sys
import time 

class User(object):
	
	def __init__(self):
		self.name = ""

	def initiate_chatapp(self, app):
		print("initiated chatapp")
		username = raw_input("Please input your name: ").strip()
		app.register_user(username)

		cmd = raw_input("please input a command: ").strip()
		if cmd == "show users":
			print(app.show_users())
