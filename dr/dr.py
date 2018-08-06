# dr
# The simple ed-like devRant client

# Import required libs
import devRantSimple as dRS			# Main backend lib / api wrapper
import commandeler as commandeler	# The Command Handeler
import globals as glbl				# All global vars are here
# Imports used for auto-login
import os							# os interfaces
from pathlib import Path			# used for finding home path
import specall as specall			# Automated api calling

# Attempt to auto-login

# Find home path
home = str(Path.home())

# Check if config exsists
if os.path.exists(home +'/.dr.conf'):
	with open(home + '/.dr.conf') as f:
		# load each line into array and remove \n
		content = f.readlines()
		content = [x.strip() for x in content]
		
		# Log in and if successfull, save credentials to global var
		creds = dRS.login(content[0], content[1])
		if creds != dRS.InvalidResponse:
			# Welcome the user
			print("Welcome @" + content[0] + "!")
			glbl.credentials = creds
			glbl.isLoggedIn = True
		else:
			# Force close with code 1
			print("Invalid login Info in config file")
			exit(1)

# Start up the threads
glbl.check_notifs = specall.getNotifs()
glbl.check_comments = specall.getComments()

glbl.check_notifs.start()
glbl.check_comments.start()

# Command prompt / main loop
#set default feed
glbl.currentFeed = dRS.RantType.algo

def prompt():
	return input(">")	# show a simple prompt

while True:
	# make sure you are using a valid item id
	if glbl.feedItemId <= 0:
		glbl.feedItemId = 1
	
	command = prompt()
	if commandeler.isValidCommand(command):
		commandeler.execute(command)
	else:
		print("?")