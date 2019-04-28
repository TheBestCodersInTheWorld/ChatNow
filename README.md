# TSChatNow
TS Chatnow lets users create their own username, chat with friends and family, and order tessert (tacos and dessert)

## Running 

### navigate to the correct directory
cd Desktop
cd TSChatNow
cd src

you can use cmd + n will get you a new terminal window


### start up nameserver
python -m Pyro4.naming 

### start the app server
python server.py

### start the client
python start.py

## Collaboration

### How can I work with Anthony?
when you open a new terminal, you'll be at your *root of your project folder*
first thing we want to do is navigtate to the project folder so 
enter these commands into the terminal

'cd Desktop'
'cd TSChatNow'

If you run the ls command:
'ls'
It should show you the contents of the directory (folder) you are in

Now there are a couple things you can do, you can try to push changes or 
receive them.

### Trying to push changes (easy way)
Enter these commands into your terminal when you are at the *root of your project folder*:
'git add -A'
'git commit -m "<insert some message here that starts with a capital verb>" '
'git push'

### Try to pull changes (easy way)
Enter these commands into your terminal when you are at your *root of your project folder*:
'git pull'

### Pulling changes didn't really work for some reason, force pull (easy way)
Enter these commands into your terminal when you are at your *root of your project folder*:
'git fetch origin master'
'git reset --hard FETCH_HEAD'
'git clean -df'