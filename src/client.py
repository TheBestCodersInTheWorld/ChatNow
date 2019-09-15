from __future__ import print_function 
import sys
import time 

SPACE = " "

class User(object):
	
	def __init__(self):
		self.name = ""

	def initiate_chatapp(self, app):
		print("initiated chatapp")
		username = raw_input("Please input your name: ").strip()
		self.name = username
		app.register_user(username)

		while (True):
			messages = app.receive_messages(self.name)
			print("\nThese are the messages you got: ")
			for message in messages:
				print(message)

			print("\n")

			self.menu()
			# this takes the input from the user and makes cmd that input result
			cmd = raw_input("please input a command: ").strip()

			# if the user specified show users as an option
			if cmd == "show users" or cmd == "s":
				print(app.show_users())
			elif cmd == "text a user" or cmd == "t":
				# print("The format should be like: @<username> \"<message you want to send>\" ")
				# TODO: list all the different flag options they can use 
				# -m => message 
				message = raw_input("please input a message: ").strip()
				receiver = raw_input("who are you sending this message to: ").strip()

				app.send_message(self.name, receiver, message)
			# TODO: add more possible commands



	def menu(self):
		print("here are some choices")
		print("s | show users")
		print("t | text a user")


	# very simplistic but inefficient way of parsing the input
	def parse_message(self, message_input):
		username = ""
		message = ""
		for index in range(len(message_input)):
			character = message_input[index]
			# if the index is 0 and the character is @
			if index == 0:
				if character != "@":
					raise Exception("Error: message format is not correct")
				else:
					new_index = index + 1
					while character != SPACE:
						character = message_input[new_index]
						username += character
						new_index += 1
			if character == "\"":
				new_index = index + 1
				character = message_input[new_index]
				while character != "\"":
					character = message_input[new_index]
					message += character
					new_index += 1
		return username, message










