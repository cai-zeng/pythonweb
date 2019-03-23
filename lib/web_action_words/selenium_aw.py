from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selenium(object):
    def __init__(self):
        self.version = ''
        self.drivers = {}
        self.current_driver = ''

    def find_element(self, method, locator, timeout):
        # 通过方法和传入的值，查找元素
        driver = self.drivers[self.current_driver]
        driver.implicitly_wait(0.5)
        find_frequency = 0.5
        try:
            element = WebDriverWait(driver, timeout, find_frequency).until(lambda x: driver.find_element(method, locator))
        except:
            element = None
        return element

    def find_elements(self, method, locator, timeout):
        # 通过方法和传入的值，查找并返回找到的所有元素
        driver = self.drivers[self.current_driver]
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        pass

    def wait_until_element_enable(self, method, locator, timeout):
        # 等待元素使能
        pass

    def wait_until_element_visible(self, method, locator, timeout):
        # 等待元素可见
        pass

    def wait_until_element_enable_and_click(self, method, locator, timeout):
        pass

