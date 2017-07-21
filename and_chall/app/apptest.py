import unittest,models
from models import user, buckets,storage


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
