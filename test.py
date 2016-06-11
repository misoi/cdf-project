from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
	# ensure that flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/index', content_type='html/text')
		self.assertEqual(response.status_code, 200)

		
       # ensure page loads correctly
	def test_home_page(self):
		tester = app.test_client(self)
		response = tester.get('/index', content_type='html/text')
		self.assertTrue(b'please login' in response.data)

if __name__ == '__main__':
	unittest.main() 
		