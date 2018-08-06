import commands as c		# All program commands
import globals as glbl		# Global vars
import devRantSimple as dRS	# Main backend

validCommands = ["q", "r", "t", "p!", "p", "st", "sr", "sa", "v", "v+", "v-", "l", "c", "pc", "n", "+", "-", "vi", "vc", "vc!", "n!"]

# COMMAND LIST
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
# pc - post comment
# n - notif feed
# + - upvote
# - - downvote glbl.currentid
# vi - view id (prompt)
# vc - view all comments on current rant
# vc! - force load comments (slower)
# n! - clear notifs

def isValidCommand(command):
	if len(command) > 0:
		return command in validCommands
	else:
		return False

def execute(command):
	if command == "q":
		c.quit()
	if command == "r":
		c.newRant()
	if command == "t":
		c.addTags()
	if command == "p!":
		c.postRant()
	if command == "p":
		response = input("Are you sure? (Y/N):")
		if response == "y" or response == "Y":
			c.postRant()
	if command[0] == "s":
		if len(command) == 2:
			if command[1] == "a":
				glbl.currentFeed = dRS.RantType.algo
			if command[1] == "t":
				glbl.currentFeed = dRS.RantType.top
			if command[1] == "r":
				glbl.currentFeed = dRS.RantType.recent
		else:
			print("?")
	if command[0] == "v" and command != "vi" and command != "vc":
		c.viewFromFeed(command)
	if command == "l":
		c.login()
	if command == "c":
		response = input("Are you sure? (Y/N):")
		if response == "y" or response == "Y":
			c.newComment()
	if command == "pc":
		c.postComment()
	if command == "n":
		c.viewMtNotifs()
	if command == "+":
		c.upVote()
	if command == "-":
		c.downVote()
	if command == "vi":
		c.viewRantById()
	if command == "vc":
		c.viewMtComments()
	if command == "vc!":
		c.viewComments()
	if command == "n!":
		c.clearNotifs()