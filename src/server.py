from __future__ import print_function
import Pyro4
from collections import defaultdict


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class AppServer(object):
	def __init__(self):
		# just a placeholder
		# self.usernames = []
		# TODO: think of a better name
		self.strucmes = defaultdict(list)

	@Pyro4.expose
	def register_user(self, name):
		# self.usernames.append(name)
		self.strucmes[name]


	@Pyro4.expose
	def show_users(self):
		return self.strucmes.keys()

	@Pyro4.expose
	def send_message(self, sender, receiver, message):
		self.strucmes[receiver].append(str(sender) + message)
		print(self.strucmes)

	@Pyro4.expose
	def receive_messages(self, receiver):
		# save a copy
		print(receiver)
		messages = self.strucmes[receiver]
		print(messages)
		# delete messages
		self.strucmes[receiver] = []
		return messages



def main():
	Pyro4.Daemon.serveSimple(
		{
			AppServer: "TSChatNow"
		},
		ns = True)

if __name__ == "__main__":
	main()