import devRantSimple as dRS	# Main backend
import getpass				# Password input
import globals as glbl		# Global vars
import classRant as classes	# Class based interface to dRS


def printrant(rant):
	if bool(rant.user.isdevRantPlusPlus):
		dpp = " ++"
	else:
		dpp = ""
		
	print("@" + rant.user.username + dpp + " | Score:" + str(rant.score) + " | ID:" + dRS.genRantCode(rant.rantid))
	print(rant.body)
	print("------")
	print(rant.getTags())
	glbl.currentid = rant.rantid

def rantPrompt(title):
	print(title)
	# Temporary text storage
	tempText = ""
	typing = True
	while typing:
		inputText = input("|")
		if inputText == ".":
			typing = False
		else:
			tempText += inputText + "\n"
	return tempText

def newRant():
	# make a new blank rant
	glbl.rantToPost = classes.NewRant("","")
	rantBody = rantPrompt("Rant Body:")
	glbl.rantToPost.body = rantBody

def addTags():
	print("Add Tags (comma seperated):")
	glbl.rantToPost.tags = input("|")

def postRant():
	if glbl.isLoggedIn:
		# Get auth data
		uid = glbl.credentials["user_id"]
		token = glbl.credentials["token_id"]
		key = glbl.credentials["token_key"]
		response = dRS.postRant(glbl.rantToPost.body, glbl.rantToPost.tags, uid, token, key)
		if response["success"]:
			print("Posted!")
		else:
			print("Something Went Wrong")
			print("Data From Server:")
			print(response)
	else:
		print("Not Logged In")

def viewFromFeed(command):
	if len(command) == 2:
		if command[1] == "+":
			glbl.feedItemId += 1
		elif command[1] == "-":
			glbl.feedItemId -= 1
	
	# Turn rant data from api into rant class
	rant = classes.Rant(dRS.getRant(glbl.currentFeed, glbl.feedItemId)["id"])
	#print to screen
	printrant(rant)
	glbl.currentViewedRant = rant

def login():
	username = input("Username?\n>")
	password = getpass.getpass("Password?\n>")
	creds = dRS.login(username, password)
	if creds != dRS.InvalidResponse:
		print("Logged In")
		glbl.credentials = creds
		glbl.isLoggedIn = True

def newComment():
	glbl.commentToPost = rantPrompt("Comment Body:")

def postComment():
	if glbl.isLoggedIn:
		# Get auth data
		uid = glbl.credentials["user_id"]
		token = glbl.credentials["token_id"]
		key = glbl.credentials["token_key"]
		response = dRS.comment(glbl.currentViewedRant.rantid, glbl.commentToPost, uid, token, key)
		if response["success"]:
			print("Posted!")
		else:
			print("Something Went Wrong")
			print("Data From Server:")
			print(response)
	else:
		print("Not Logged In")

def viewNotifs():
	print("Fetching Notifs. Please Wait...")
	if glbl.isLoggedIn:
		uid = glbl.credentials["user_id"]
		token = glbl.credentials["token_id"]
		key = glbl.credentials["token_key"]
		response = dRS.getNotifs(uid, token, key)
		items = response["data"]["items"]
		i = 0
		while i < len(items):
			if not bool(items[i]["read"]):
				notif = (classes.Notif(items[i]))
				if notif.contentType == dRS.NotifType.sub:
					print("------------")
					print("@" + notif.username + ": Posted a new rant")
					print("rantCode:" + str(dRS.genRantCode(notif.rantId)))
				if notif.contentType == dRS.NotifType.mention:
					print("------------")
					print("@" + notif.username + ": Mentioned you in a comment")
					commentdata = dRS.getIdComment(notif.rantId, notif.commentId, uid, token, key)
					comment = classes.Comment(commentdata["comment"])
					print(comment.body)
					print("rantCode:" + str(dRS.genRantCode(notif.rantId)))
				if notif.contentType == dRS.NotifType.content:
					print("------------")
					print("@" + notif.username + ": Commented on your rant")
					print("rantCode:" + str(dRS.genRantCode(notif.rantId)))
				if notif.contentType == dRS.NotifType.vote:
					print("------------")
					print("@" + notif.username + ": Upvoted one of your rants")
			i+=1

def upVote():
	rantid = glbl.currentViewedRant.rantid
	if rantid == 00:
		print("Unable To Place Vote")
	else:
		if glbl.isLoggedIn:
			uid = glbl.credentials["user_id"]
			token = glbl.credentials["token_id"]
			key = glbl.credentials["token_key"]
			response = dRS.vote(rantid, uid, token, key, 1)
			if response["success"]:
				print("Done")
		else:
			print("Not Logged In")

def downVote():
	rantid = glbl.currentViewedRant.rantid
	if rantid == 00:
		print("Unable To Place Vote")
	else:
		if glbl.isLoggedIn:
			uid = glbl.credentials["user_id"]
			token = glbl.credentials["token_id"]
			key = glbl.credentials["token_key"]
			response = dRS.vote(rantid, uid, token, key, -1)
			if response["success"]:
				print("Done")
		else:
			print("Not Logged In")

def viewRantById():
	print("rantCode:")
	rantCode = input(">")
	rant = classes.Rant(dRS.genRantId(rantCode))
	printrant(rant)
	glbl.currentViewedRant = rant

def viewComments():
	glbl.currentViewedRant.printAndLoadComments()

def clearNotifs():
	if glbl.isLoggedIn:
		uid = glbl.credentials["user_id"]
		token = glbl.credentials["token_id"]
		key = glbl.credentials["token_key"]
		response = dRS.clearNotifs(uid, token, key)