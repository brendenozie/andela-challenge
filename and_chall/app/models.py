import json

class User(object):

    def __init__(self, username , password):
        self.username = username
        self.password = password

    def login(self,username,password):
	if (username==username && password==password):
		return ("%s %s" % (self.first_name,self.last_name))
	else:
		return ("Invalid Username")


    def register(self,username,password):
	if (username==username && password==password):
		return ("%s %s" % (self.first_name,self.last_name))
	else:
		return ("Invalid Username")

    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getUserDetails(self):
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result

class bucket:
	def __init__:
		
	def addTask:

	def addAct:

	def deleteTask:

	def deleteAct:
