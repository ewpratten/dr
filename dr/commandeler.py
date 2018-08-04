import commands as c
import globals as glbl
import devRantSimple as dRS

CommandList = ["q", "r", "v", "p", "t", "s", "l", "c", "+", "-", "n"]
RantFeeds = [dRS.RantType.algo, dRS.RantType.top, dRS.RantType.recent]

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
# n! - clear notifs

def isValidCommand(command):
	if len(command) > 0:
		return command[0] in CommandList	#is the first char a valid command?
	else:
		return False

def execute(command, vid):
	if command == "vc":
		c.viewComments()
	if command == "vi":
		rid = input("Rant Id:\n>")
		c.viewId(rid)

	if command == "+":
		c.upVote(glbl.currentid)
	if command == "-":
		c.downVote(glbl.currentid)
	if command[0] == "n":
		if command == "n!":
			c.clearNotifs()
		else:
			c.getNotifs()
			c.dispNotifs()
	if command == "pc":
		resp = input("Are you sure? (Y/N):")
		if resp == "y" or resp == "Y":
			c.postComment(glbl.currentid)
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
	if command[0] == "v" and command != "vi" and command != "vc":
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
	