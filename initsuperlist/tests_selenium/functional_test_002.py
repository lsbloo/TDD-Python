from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000/home/')

        self.assertIn('To-Do lists', self.browser.title)
        #self.fail('Finish Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    

