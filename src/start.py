import sys 
import Pyro4
import Pyro4.util
import sys 
from client import User 

nameserver = Pyro4.locateNS()
uri = nameserver.lookup("TSChatNow")
# this is the ts chat now server 
app = Pyro4.Proxy(uri)
user = User()
user.initiate_chatapp(app)
