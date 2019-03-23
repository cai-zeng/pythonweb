from selenium import webdriver

class SeleniumUse(object):
  self.driver = webdriver.Firefox()
  url='www.baidu.com'
  self.driver.get(url)
  self.driver.implicitly_wait(timeout)
  def selenium_find_elements(self, driver, method, locator, timeout)
    element = self.driver.find_element(by=by_method, value=locator)
    return element
  selenium_find_elements('xpath', "//div[@class='btn-box']/span[@class='undefined']")
  
  # xpath示例：
  # //span[contains(@class,'setting ng-star-inserted')] 单条件
  # //div[text()='abc'] 单条件
  # //*[@class='ui-button-text'][text()='abc'] 组合条件
"""  
1.	基本写法，//label[@id=’ISM’]    //label[text()=’ISM’]
2.	多条件写法，//td[@name=’’ and @title=’’] 或 //td[@name=’’][@ title=’’]
3.	/ 与 // 区别，/只匹配儿子节点，不匹配孙子节点；
4.	/parent::*或者/..  父节点
5.	/following-sibling::td向后找兄弟节点
6.	/preceding-sibling::td向前找兄弟节点
7.	last()           //td[last()]最后一个节点
8.	contains()        //td[contains(text(),’ISM’)]文本包含
9.	normalize-space去两头空格  //label[normalize-space(@title)='确定']
"""
