import devRantSimple as dRS
import getpass
import globals as glbl
import classes as classes

# commands

def printrant(rant):
	# if "joke/meme" not in rant["tags"]:
	# print(rant)
	print("@" + rant["username"])
	print(rant["text"])
	print(rant["tags"])
	glbl.currentid = rant["id"]

def command_view(command, viewid, sort):
	if len(command) == 1:
		rant = dRS.getRant(sort, viewid)
		printrant(rant)
		return viewid
	elif command[1] == "+":
		viewid += 1
		rant = dRS.getRant(sort, viewid)
		printrant(rant)
		return viewid
	else:
		viewid -= 1
		rant = dRS.getRant(sort, viewid)
		printrant(rant)
		return viewid

def viewId(rid):
	rant = dRS.getRantFromId(rid)
	printrant(rant)
	glbl.currentid = rid

def login():
	username = input("Username?\n>")
	password = getpass.getpass("Password?\n>")
	creds = dRS.login(username, password)
	if creds != dRS.InvalidResponse:
		print("Logged In")
		glbl.creds = creds
		glbl.isloggedin = True

def post():
	if glbl.isloggedin:
		uid = glbl.creds["user_id"]
		token = glbl.creds["token_id"]
		key = glbl.creds["token_key"]
		response = dRS.postRant(glbl.rant_text, glbl.rant_tags, uid, token, key)
		if response["success"]:
			glbl.rant_text = ""
			print("Done")
	else:
		print("Not Logged In")
	
def newRant():
	print("Rant Body:")
	rtype = True
	while rtype:
		inp = input("|")
		if inp == ".":
			rtype = False
		else:
			glbl.rant_text += inp + "\n"
	
def newTags():
	print("Add Tags (comma seperated)")
	glbl.rant_tags = input("|")

	
def newComment(viewid, sort):
	username = dRS.getRant(sort, viewid)
	username = username["username"]
	print("Comment On @" + username + "'s Rant:")
	rtype = True
	while rtype:
		inp = input("|")
		if inp == ".":
			rtype = False
		else:
			glbl.rant_comment += inp + "\n"

def postComment(rantid):
	if glbl.isloggedin:
		uid = glbl.creds["user_id"]
		token = glbl.creds["token_id"]
		key = glbl.creds["token_key"]
		response = dRS.comment(rantid, glbl.rant_comment, uid, token, key)
		if response["success"]:
			glbl.rant_comment = ""
			print("Done")
	else:
		print("Not Logged In")

def getNotifs():
	print("Fetching Notifs...")
	if glbl.isloggedin:
		uid = glbl.creds["user_id"]
		token = glbl.creds["token_id"]
		key = glbl.creds["token_key"]
		response = dRS.getNotifs(uid, token, key)
		items = response["data"]["items"]
		i = 0
		while i < len(items):
			if not bool(items[i]["read"]):
				glbl.notifs.append(classes.Notif(items[i]))
			i+=1

def dispNotifs():
	uid = glbl.creds["user_id"]
	token = glbl.creds["token_id"]
	key = glbl.creds["token_key"]
	i = 0
	while i < len(glbl.notifs):
		notif = glbl.notifs[i]
		if not notif.isItRead():
			if notif.getType() == dRS.NotifType.sub:
				print("------------")
				print("@" + notif.getUsername() + ": Posted a new rant")
				print("Rant Id:" + str(notif.getId()))
			if notif.getType() == dRS.NotifType.mention:
				print("------------")
				print("@" + notif.getUsername() + ": Mentioned you in a comment")
				# dRS.getIdComment(notif.rantId, notif.commentId, uid, token, key)
				print("(Unable to fetch preview)")
				print("Rant Id:" + str(notif.getId()))
			if notif.getType() == dRS.NotifType.content:
				print("------------")
				print("@" + notif.getUsername() + ": Commented on your rant")
				print("Rant Id:" + str(notif.getId()))
			if notif.getType() == dRS.NotifType.vote:
				print("------------")
				print("@" + notif.getUsername() + ": Upvoted one of your rants")
		i +=1

def upVote(rantid):
	if rantid == 00:
		print("Unable To Place Vote")
	else:
		if glbl.isloggedin:
			uid = glbl.creds["user_id"]
			token = glbl.creds["token_id"]
			key = glbl.creds["token_key"]
			response = dRS.vote(rantid, uid, token, key, 1)
			if response["success"]:
				print("Done")
		else:
			print("Not Logged In")

def downVote(rantid):
	if rantid == 00:
		print("Unable To Place Vote")
	else:
		if glbl.isloggedin:
			uid = glbl.creds["user_id"]
			token = glbl.creds["token_id"]
			key = glbl.creds["token_key"]
			response = dRS.vote(rantid, uid, token, key, -1)
			if response["success"]:
				print("Done")
		else:
			print("Not Logged In")