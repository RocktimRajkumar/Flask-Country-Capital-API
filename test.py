# importing module
from app import app
import unittest


class CountryCapitalTestCase(unittest.TestCase):
    
    # testing index page response
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


# test case entry point
if __name__ == '__main__':
    unittest.main()
