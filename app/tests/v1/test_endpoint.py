import os
import json
import datetime
from app import appCreate

import unittest


class TestEndpoints(unittest.TestCase):

    def setup(self):
        self.app = appCreate()
        self.client = self.app.test_client()
        
    def test_getallredflags(self):
        self.app = appCreate()
        self.client = self.app.test_client
        response = self.client().get('/red_flags')
        self.assertEqual(response.status_code, 200)
    def test_getredflagsbyid(self):
        self.app = appCreate()
        self.client = self.app.test_client
        response = self.client().post('/<int:RedFlagsid>',data=json.dumps({
                
	            "name": "trim",
	            "flag": "redflag",
	            "location": "jose@gmail.com"
	

            }),headers={'content-type': 'application/json'})
        item = self.client().get('/1')

        self.assertEqual(item.status_code, 200)
        
    def test_postnewredflag(self):
        self.app = appCreate()
        self.client = self.app.test_client
        response = self.client().post('/red_flags',data=json.dumps({
                
	            "name": "trim",
	            "flag": "redflag",
	            "location": "jose@gmail.com"
	

            }),headers={'content-type': 'application/json'})
        self.assertEqual(response.status_code,201)
    
    def test_deleteredflagbyid(self):
        self.app = appCreate()
        self.client = self.app.test_client
        response = self.client().delete('/1')
        item = self.client().get('/1')
        self.assertEqual(item.status_code,200)

    def test_patchbyid(self):
        self.app = appCreate()
        self.client = self.app.test_client
        response = self.client().patch('/<int:RedFlagsid>',data=json.dumps({
                
	            "name": "trim",
	            "comment": "holla",
	            "location": "jose@gmail.com"
	

            }),headers={'content-type': 'application/json'})

        item = self.client().get('/1')
        self.assertEqual(item.status_code,200)
    
if __name__=='__main__':
    unittest.main()