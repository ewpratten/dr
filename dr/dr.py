# dr
# by: Evan Pratten <ewpratten>
import devRantSimple as dRS
from enum import Enum
import commands as c
import globals as glbl
import os

# Vars

RantFeeds = [dRS.RantType.algo, dRS.RantType.top, dRS.RantType.recent]
InvalidCommand = False	# Set to true if user typed something wrong
running = True			# Used to controlcommand loop
glbl.CurrentSection = dRS.RantType.algo
glbl.ViewId = 1

CommandList = ["q", "r", "v", "p", "t", "s", "l", "c", "+", "-"]

# q - quit
# r - new rant
# t - add tags
# p! - post without varification
# p - post (Y/N) if y, post
# s - section to view from (top, recent, algo) (t, r, a)
# v - view current
# v+ - view next
# v- - view prev
# l - login
# c - comment on current rant
# c! - comment post
# + - upvote
# - - downvote

#only check first char, others are checked in execute

# commands
import commands

# Functions
def prompt():
	return input(">")	# show a simple prompt

def isValidCommand(command):
	if len(command) > 0:
		return command[0] in CommandList	#is the first char a valid command?
	else:
		return False

def execute(command, vid):
	if command == "pc":
		resp = input("Are you sure? (Y/N):")
		if resp == "y" or resp == "Y":
			c.postComment(vid, glbl.CurrentSection)
	if command == "c":
		c.newComment(vid, glbl.CurrentSection)
	if command[0] == "l":
		c.login()
	if command[0] == "r":
		c.newRant()
	if command[0] == "t":
		c.newTags()
	if command == "p!":
		c.post()
	if command == "p":
		resp = input("Are you sure? (Y/N):")
		if resp == "y" or resp == "Y":
			c.post()
	if command[0] == "q":
		exit()
	if command[0] == "v":
		glbl.ViewId = c.command_view(command, vid, glbl.CurrentSection)
	if command[0] == "s":
		if len(command) == 2:
			if command[1] == "a":
				glbl.CurrentSection = dRS.RantType.algo
			if command[1] == "t":
				glbl.CurrentSection = dRS.RantType.top
			if command[1] == "r":
				glbl.CurrentSection = dRS.RantType.recent
		else:
			print("?")
	

## STARTUP ##
# check if login config exsists
# if not, create
from pathlib import Path
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
	if glbl.ViewId < 1:
		glbl.ViewId = 1
	
	command = prompt()
	if isValidCommand(command):
		execute(command, glbl.ViewId)
	else:
		print("?")
		InvalidCommand = True

# return values
if not running:
	print("")
else:
	print("Program crashed outside main loop")