import unittest


class user(object):
	def __init__(self,name,password,userId):
		self.name=name
		self.password=password
		self.userId=userId


	def addUser():
		newUser={
                'userName': self.name,
                'userId': self.userId,
                'upass': self.password
		}
		
		storage.users.append(newUser)

	#def delUser():
	
	

class accounts():
	def login(username,password):
		if (self.username==username and self.password==password):
			pass
		else:
			return "Incorrect username or password"
	def logout():
			return 


class buckets():
	def __init__(self,bucName,bucId,bucDueDate):
		self.bucName=bucName
		self.bucId=bucId
		self.bucDueDate=bucDueDate
		
	def saveAct(self,bucName,bucId,bucDueDate):
		newBuc={
                'bucName': self.bucName,
                'bucId': self.bucId,
                'bucDueDate': self.bucDueDate}
		
		storage.buckets.append(newBuc)
		
	def delAct():
		view = [ bucName for bucName in storage.buckets]
        	del bucName
        	print "done"
		
	
		
	def viewAct():
		dataList = storage.buckets
		for index in range(len(dataList)):
    			for key in dataList[index]:
        			print(dataList[index][key])

	



class task():

	def __init__(self,taskName,taskId,taskDueDate):
		self.taskName=taskName
		self.taskDueDate=taskDueDate
		self.taskId=taskId
		
		

	def savetask():
		newtask={
                'taskName': self.taskName,
                'bucId': self.bucId,
                'taskId': self.taskId}
        	storage.tasks.append(newtask)


	def delTask():
		Task = [ taskName for taskName in storage.tasks]
		del Task
        	print "done"



	def viewTask():
		dataList = storage.tasks
		for index in range(len(dataList)):
    			for key in dataList[index]:
        			print(dataList[index][key])


	

class storage():
	tasks=[]
	buckets=[]
	users=[]






