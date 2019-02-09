import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.baidu.com')
        elem = self.browser.find_element_by_id('kw')
        elem.send_keys('CWT'+Keys.RETURN)
        sleep(10)

        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)