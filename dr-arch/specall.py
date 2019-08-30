# specall
from threading import Thread
import time
import dr.globals as glbl
import classRant as classes
import devRantSimple as dRS

def getNotifsToGlbl():
	if glbl.isLoggedIn:
		uid = glbl.credentials["user_id"]
		token = glbl.credentials["token_id"]
		key = glbl.credentials["token_key"]
		response = dRS.getNotifs(uid, token, key)
		items = response["data"]["items"]
		i = 0
		while i < len(items):
			if not bool(items[i]["read"]):
				glbl.notifs.append(classes.Notif(items[i]))
				# print(i)
			i+=1

def getCommentsToGlbl():
	if glbl.currentViewedRant != "":
		comments = glbl.currentViewedRant.comments
		glbl.currentViewedRant.comments = []
		i = 0
		glbl.commentLen = len(comments)
		while i < len(comments):
			# print(i)
			glbl.currentViewedRant.comments.append(classes.Comment(comments[i]))
			# print(glbl.currentViewedRant.comments)
			i+=1

class getNotifs(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.running = True

	def run(self):
		while self.running:
			getNotifsToGlbl()
			i = 0
			# Cheaty way to get around not being able to kill a thread with a timer
			while i < glbl.notifInterval and self.running:
				time.sleep(1)
				i+=1
	def stop(self):
		self.running = False


class getComments(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.running = True

	def run(self):
		getCommentsToGlbl()
	def stop(self):
		self.running = False
