import unittest
import json
from app import app

class TestApp(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True
  
  def Test_Case_1(self):
    payload = {"a": 5, "b": 6, "operator":"+"}
    response = self.app.post('/lab15_16/operation/', data=json.dumps(payload), content_type='app')
    self.assertIn(response.status_code, [200, 201])
    data = response.get_json()
    self.assertEqual(data['result'], '11')
  
  def Test_Case_2(self):
    payload = {"a": 11, "b": 8, "operator":"-"}
    response = self.app.post('/lab15_16/operation/', data=json.dumps(payload), content_type='app')
    self.assertIn(response.status_code, [200, 201])
    data = response.get_json()
    self.assertEqual(data['result'], '3')
  
  def Test_Case_3(self):
    payload = {"a": 2, "b": 2, "operator":"ddd"}
    response = self.app.post('/lab15_16/operation/', data=json.dumps(payload), content_type='app')
    self.assertIn(response.status_code, [200, 201])
    data = response.get_json()
    self.assertEqual(data['result'], 'unknown')
  
