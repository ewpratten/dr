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

# class Comment(object):
	
# 	def __init__(self, )

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
	
	def getContents(self):
		print("hi")

# deb
u1 = User("ewpratten")