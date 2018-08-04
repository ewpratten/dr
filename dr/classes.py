import devRantSimple as dRS

class User(object):
	
	def __init__(self, username):
		raw = dRS.getUserData(dRS.getUserId(username), {"app":3})
		self.username = raw["profile"]["username"]
		self.user_score = raw["profile"]["score"]
		self.about = raw["profile"]["about"]
		self.skills = raw["profile"]["skills"]
		self.dpp = raw["profile"]["dpp"]
	
	def isPlusPlus(self):
		return bool(self.dpp)
	
	def getScore(self):
		return self.user_score
	
	def getBio(self):
		return [self.about, self.skills]
	
	def getUsername(self):
		return self.username

class Comment(object):
	
	def __init__(self, commentdata):
		self.body = commentdata["body"]
		self.commentid = commentdata["id"]
		self.rantid = commentdata["rant_id"]
		self.score = commentdata["score"]
		self.user = User(commentdata["user_username"])

class Notif(object):
	
	def __init__(self, item_in):
		item = item_in
		self.time = item["created_time"]
		self.content = item["type"]
		
			
		if self.content == "rant_sub":
			self.content = dRS.NotifType.sub
		if self.content == "comment_content":
			self.content = dRS.NotifType.content
		if self.content == "content_vote":
			self.content = dRS.NotifType.vote
		if self.content == "comment_mention":
			self.content = dRS.NotifType.mention
		self.isRead = bool(item["read"])
		if self.content != dRS.NotifType.sub and self.content != dRS.NotifType.vote and self.content != "comment_discuss":
			# print(item)
			self.commentId = item["comment_id"]
		
		self.rantId = item["rant_id"]
		self.userId = item["uid"]
		self.username = dRS.getUserData(self.userId, {"app":3})["profile"]["username"]
	
	def getUsername(self):
		return self.username
	
	def getType(self):
		return self.content
	
	def isItRead(self):
		return self.isRead
	
	def getId(self):
		return self.rantId
	

class Rant(object):
	
	def __init__(self, rantid):
		self.rantid = rantid
		self.rantCode = dRS.genRantCode(rantid)
		rant = dRS.getRantFromId(self.rantid)
		self.body = rant["text"]
		self.score = rant["score"]
		self.user = rant["username"]
		self.user = User(self.user)
		self.tags = rant["tags"]
		self.comments = rant["comments"]
	
	def loadComments(self):
		print("Fetching Comments. Please Wait...", end="")
		comments = self.comments
		# print(comments)
		self.comments = []
		i = 0
		while i < len(comments):
			self.comments.append(Comment(comments[i]))
			i+=1
		print("")
	
	def printComments(self):
		i = 0
		while i < len(self.comments):
			print("-------")
			if bool(self.comments[i].user.dpp):
				dpp = " ++"
			else:
				dpp = ""
				
			print("@" + self.comments[i].user.username + dpp + " | Score:" + str(self.comments[i].score))
			print(self.comments[i].body)
			i+=1
	
	def getTags(self):
		i = 0
		ret = ""
		while i < len(self.tags):
			ret += self.tags[i] + ", "
			i+=1
		return ret
