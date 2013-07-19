#!/usr/bin/python

from server import app
import unittest

class ViewTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        
#     def tearDown(self):
#         print 'teardown ViewTestCase'
        
    def test_users(self):
        view = self.app.get('/api/users')
        expected = '[{"password": "pass1", "id": "1", "name": "dustin"}, {"password": "Pass2", "id": "2", "name": "leah"}]'
        actual = view.data
        self.assertEqual(expected,actual,'request for /api/users failed')
        
    def test_home(self):
        view = self.app.get('/app/views/public/home.html')
        expected = '<div> This is Home Page </div>'
        actual = view.data
        self.assertEqual(expected,actual,'request for /app/views/public/home.html failed')
        
    def test_about(self):
        view = self.app.get('/app/views/public/about.html')
        expected = '<div> This is About Page </div>'
        actual = view.data
        self.assertEqual(expected,actual,'request for /app/views/public/about.html failed')
        
#     def login(self, username):
#         return self.app.post('/login', data=dict(
#             username=username
#         ), follow_redirects=True)
# 
#     def logout(self):
#         return self.app.get('/logout', follow_redirects=True)
# 
#     def test_login_logout(self):
#         rv = self.login('admin')
# #        print rv.data
#         assert 'Logged in as admin' in rv.data
#         rv = self.logout()
# #        print rv.data
#         assert 'Logged in as None' in rv.data
       
if __name__ == '__main__':
    unittest.main()