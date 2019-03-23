from lib.web_action_words.selenium_aw import Selenium
from lib.parameters import Parameters as PARAM


class WebCommon(Selenium):

    def __init__(self):
        self.version = ''
        self.drivers = {}
        self.current_driver = ''

    def login(self, username=None, password=None):
        if username is None:
            username = PARAM.RY_USERNAME
        if password is None:
            password = PARAM.RY_PASSWORD
        usname_locator = PARAM.RY_USERNAME_XPATH
        password_locator = PARAM.RY_PASSWORD_XPATH
        timeout = 15
        self.wait_until_element_enable('xpath', usname_locator, timeout)

        self.wait_until_element_enable('xpath', password_locator, timeout)
