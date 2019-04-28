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



	def menu(self):
		print("here are some choices")
		print("s | show users")

	def make_hotdog(self, hotdog_type):
		return None


# def make_hotdog(hotdog_type):
# 	return None


# make_hotdog("the hotdog is whatever")

user1 = User()
user2 = User()
user1.make_hotdog("the hotdog is spicy")
user2.make_hotdog("the hotdog is not spicy")