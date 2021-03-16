import unittest, json
from app import app

class APITest(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_publish(self):
        r = self.app.post('http://localhost:5000/api/v1/publish', headers={"Content-Type": "application/json"}, data=json.dumps({"content": "this is test content"}))
        self.assertEqual(r.status_code, 200)
            
    def test_getLast(self):
        r = self.app.get('http://localhost:5000/api/v1/getLast')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json["content"], "this is test content")

    def test_getByTime(self):
        r = self.app.post('http://localhost:5000/api/v1/getByTime', headers={"Content-Type": "application/json"}, data=json.dumps({"start": 0, "end": -1}))
        self.assertEqual(r.status_code, 200)
        # Uncomment below line to test array comparison
        # self.assertEqual(["this is test content"], r.json["content"])
         

if __name__ == '__main__':
    unittest.main()
