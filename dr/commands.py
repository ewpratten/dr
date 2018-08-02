import drif
import devRantSimple as dRS
import getpass
import globals as glbl

# commands

def printrant(rant):
	# if "joke/meme" not in rant["tags"]:
	print(rant["username"])
	print("---")
	print(rant["text"])
	print("---")
	print(rant["tags"])

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

def login():
	username = input("Username?\n>")
	password = getpass.getpass("Password?\n>")
	creds = dRS.login(username, password)
	if creds != dRS.InvalidResponse:
		print("Logged In")
		glbl.creds = creds

def post():
	uid = glbl.creds["user_id"]
	token = glbl.creds["token_id"]
	key = glbl.creds["token_key"]
	response = dRS.postRant(glbl.rant_text, glbl.rant_tags, uid, token, key)
	
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