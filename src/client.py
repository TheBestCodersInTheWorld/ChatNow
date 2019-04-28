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

		while (True):
			self.menu()
			# this takes the input from the user and makes cmd that input result
			cmd = raw_input("please input a command: ").strip()

			# if the user specified show users as an option
			if cmd == "show users" or cmd == "s":
				print(app.show_users())
			# TODO: add more possible commands



	def menu(self):
		print("here are some choices")
		print("s | show users")
