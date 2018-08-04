# dr
# by: Evan Pratten <ewpratten>
import devRantSimple as dRS
from enum import Enum
import globals as glbl
import os
from pathlib import Path
import commandeler as commandeler

# Vars
InvalidCommand = False	# Set to true if user typed something wrong
running = True			# Used to controlcommand loop
glbl.CurrentSection = dRS.RantType.algo
glbl.ViewId = 1

# Command Prompt
def prompt():
	return input(">")	# show a simple prompt

## STARTUP ##
# check if login config exsists
# login
home = str(Path.home())

if os.path.exists(home +'/.dr.conf'):
	with open(home + '/.dr.conf') as f:
		content = f.readlines()
		content = [x.strip() for x in content]
		
		creds = dRS.login(content[0], content[1])
		if creds != dRS.InvalidResponse:
			print("Welcome @" + content[0] + "!")
			glbl.creds = creds
			glbl.isloggedin = True
	

## MAIN LOOP ##
while running:
	# make sure you are using a valid view id
	if glbl.ViewId < 1:
		glbl.ViewId = 1
	
	command = prompt()
	if commandeler.isValidCommand(command):
		commandeler.execute(command, glbl.ViewId)
	else:
		print("?")
		InvalidCommand = True

# return values
if not running:
	print("")
else:
	print("Program crashed outside main loop")