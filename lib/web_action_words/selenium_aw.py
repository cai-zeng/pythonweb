from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selenium(object):
    def __init__(self):
        self.version = ''
        self.drivers = {}
        self.current_driver = ''

    # ----------------------------------浏览器操作类----------------------------------------------------------------------

    def open_browser(self, url, alias, browser_type='Firefox', timeout=15):
        """
        打开浏览器并访问url链接
        :param url: 要访问的浏览起链接
        :param alias: 浏览器别称。便于多个浏览器测试，每次打开浏览器时需要输入别称，且别称不能同名
        :param browser_type: 浏览器类型，只支持 Firefox，Chrome，IE
        :param timeout: 打开url的超时时间
        :return: 浏览器对象
        """
        if browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif browser_type == 'IE':
            driver = webdriver.Ie()
        else:
            raise ("不支持的浏览器类型：%s" % browser_type)

        driver.get(url)
        self.__register_browser(driver, alias)
        self.switch_browser(alias)
        return driver

    def __register_browser(self, driver, alias):
        self.drivers[alias] = driver

    def switch_browser(self, alias):
        self.current_driver = alias

    def close_browser(self, alias):
        self.drivers[alias].quit()
        self.drivers.pop(alias)

    # ----------------------------------元素操作类-----------------------------------------------------------------------

    def find_element(self, method, locator, timeout=0):
        # 通过方法和传入的值，查找元素
        driver = self.drivers[self.current_driver]
        driver.implicitly_wait(0.5)
        find_frequency = 0.5
        try:
            element = WebDriverWait(driver, timeout, find_frequency).until(lambda x: x.find_element(method, locator))
        except:
            element = None
        return element

    def find_elements(self, method, locator, timeout):
        # 通过方法和传入的值，查找并返回找到的所有元素
        driver = self.drivers[self.current_driver]
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        pass

    def wait_until_element_enable(self, method, locator, timeout):
        #
        element = self.find_element(method, locator, timeout)
        element.is_enabled()

    def wait_until_element_visible(self, method, locator, timeout):
        # 等待元素可见
        pass

    def wait_until_element_enable_and_click(self, method, locator, timeout, Tab_key=False):
        # 等待元素可见并点击
        element = self.find_element(method, locator, timeout)
        element.click()

    def wait_until_element_enable_and_input_text(self, method, locator, timeout, value, Tab_key=False):
        # 输入值
        element = self.find_element(method, locator, timeout)
        element.send_keys(value)
        if Tab_key is True:
            element.send_keys(Keys.TAB)
