import devRantSimple as dRS
import getpass
import globals as glbl
import classes as classes

# commands


def printrant(rant):
	if bool(rant.user.dpp):
		dpp = " ++"
	else:
		dpp = ""
		
	print("@" + rant.user.username + dpp + " | Score:" + str(rant.score))
	print(rant.body)
	print("------")
	print(rant.getTags())
	glbl.currentid = rant.rantid

def command_view(command, viewid, sort):
	rant = classes.Rant(dRS.getRant(sort, viewid)["id"])
	if len(command) == 1:
		printrant(rant)
	elif command[1] == "+":
		viewid += 1
		printrant(rant)
	else:
		viewid -= 1
		printrant(rant)
	
	glbl.currentRant = rant
	return viewid

def viewId(rid):
	rant = classes.Rant(dRS.genRantId(rid))
	printrant(rant)
	glbl.currentRant = rant

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
			print("Done!")
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
	username = glbl.currentRant
	username = username.user.username
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
	print("Fetching Notifs. Please Wait...")
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

def clearNotifs():
	if glbl.isloggedin:
		uid = glbl.creds["user_id"]
		token = glbl.creds["token_id"]
		key = glbl.creds["token_key"]
		response = dRS.clearNotifs(uid, token, key)

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
				print("rantCode:" + str(dRS.genRantCode(notif.getId())))
			if notif.getType() == dRS.NotifType.mention:
				print("------------")
				print("@" + notif.getUsername() + ": Mentioned you in a comment")
				commentdata = dRS.getIdComment(notif.rantId, notif.commentId, uid, token, key)
				comment = classes.Comment(commentdata["comment"])
				print(comment.body)
				print("rantCode:" + str(dRS.genRantCode(notif.getId())))
			if notif.getType() == dRS.NotifType.content:
				print("------------")
				print("@" + notif.getUsername() + ": Commented on your rant")
				print("rantCode:" + str(dRS.genRantCode(notif.getId())))
			if notif.getType() == dRS.NotifType.vote:
				print("------------")
				print("@" + notif.getUsername() + ": Upvoted one of your rants")
		i +=1
	glbl.notifs = []

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

def viewComments():
	glbl.currentRant.loadComments()
	glbl.currentRant.printComments()