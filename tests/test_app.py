import unittest
import json
from app import app

class TestApp(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True
  
  def test_case_1(self):
    payload = {"a": 5, "b": 6, "operator":"+"}
    response = self.app.post('/lab15_16/operation/', data=json.dumps(payload), content_type='application/json')
    self.assertIn(response.status_code, [200, 201])
    data = response.get_json()
    self.assertEqual(data['result'], '11')
  
  def test_case_2(self):
    payload = {"a": 11, "b": 8, "operator":"-"}
    response = self.app.post('/lab15_16/operation/', data=json.dumps(payload), content_type='application/json')
    self.assertIn(response.status_code, [200, 201])
    data = response.get_json()
    self.assertEqual(data['result'], '3')
  
  def test_case_3(self):
    payload = {"a": 2, "b": 2, "operator":"ddd"}
    response = self.app.post('/lab15_16/operation/', data=json.dumps(payload), content_type='application/json')
    self.assertIn(response.status_code, [400, 422])
    data = response.get_json()
    self.assertEqual(data['error'], 'Invalid input')  

if __name__ =='__main':
  unittest.main()