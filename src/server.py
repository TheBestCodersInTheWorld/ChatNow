from __future__ import print_function
import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class AppServer(object):
	def __init__(self):
		# just a placeholder
		self.usernames = []

	@Pyro4.expose
	def register_user(self, name):
		self.usernames.append(name)


	@Pyro4.expose
	def show_users(self):
		return (self.usernames)

	@Pyro4.expose
	def send_message(self, username, message):
		# TODO: think about how the server can send 
		# the message to the user
		# In other words: what should we do in this function



def main():
	Pyro4.Daemon.serveSimple(
		{
			AppServer: "TSChatNow"
		},
		ns = True)

if __name__ == "__main__":
	main()