import unittest



class user(object):
 def __init__(self, name, password,userId):
    		self.name = name
		self.password=password
		self.userId=userId

 def addUser(self):
			newUser ={
                'userName': self.name,
                'userId': self.userId,
                'upass': self.password
			}
		
			storage.users.append(newUser)

 def viewUsers(self):
			dataList = storage.users
			for index in range(len(dataList)):
    				for key in dataList[index]:
    						print(dataList[index][key])
	
	


 def login(self):
	return
	

class accounts(object):
	 @classmethod
    	 def login(username,password):
    			 if (self.username==username and self.password==password):
    					 return "OK"		 
    			 else:
				         return "Incorrect username or password"
		 #def logout():
				#return 


class buckets(object):
		 @classmethod
		 def __init__(self,bucName,dueDate,bucId,userId):
				self.bucName=bucName
				self.bucId=bucId
				self.dueDate=dueDate
				self.userId=userId
		 @classmethod
		 def saveAct(self):
				newBuc={
                		'bucName': self.bucName,
                		'bucId': self.bucId,
                		'bucDueDate': self.dueDate,
				'userId':self.userId
				}
		
				storage.buckets.append(newBuc)
		
		 #def delAct(self):
    			#bcket = [ bucName for bucName in storage.buckets]
				#del bcket
				#print ("done")
		
	
		 @classmethod
		 def viewAct(self):
				dataList = storage.buckets
				for index in range(len(dataList)):
    					for key in dataList[index]:
        						print(dataList[index][key])

	
	#def createTask(self):
		


class task(object):

		@classmethod
		def __init__(self,taskName,dueDate,bucId,taskId):
				self.taskName=taskName
				self.dueDate=dueDate
				self.taskId=taskId
				self.bucId=bucId
		
		
		@classmethod
		def savetask(self):
				newtask={
                		'taskName': self.taskName,
                		'bucId': self.bucId,
                		'taskId': self.taskId,
				'Duedate':self.dueDate				
				}
        			storage.tasks.append(newtask)

		@classmethod
		def delTask(self):
				Task = [ taskName for taskName in storage.tasks]
				del Task
        		#print ("done")


		@classmethod
		def viewTask(self):
				dataList = storage.tasks
				for index in range(len(dataList)):
    					for key in dataList[index]:
        						print(dataList[index][key])


	

class storage(object):
		tasks=[]
		buckets=[]
		users=[]






class bucketTestCase(unittest.TestCase):
  
    def setUp(self):
        self.store = storage()

    def testAddUser(self):
        jane=user("jane","oloo",1)
	jane.addUser()
	crunch=user("juma","awil","wewe")
	crunch.addUser()
        result = len(self.store.users)
        self.assertEqual(result, 2)
	
	
    def testAddBucket(self):
        buc1=buckets("drive","oloo",1,232423)
	buc1.saveAct()
	buc2=buckets("juma","awil","wewe",23243242)
	buc2.saveAct()
        result = len(self.store.buckets)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()




