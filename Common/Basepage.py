import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from Common import config
from selenium.webdriver.support import expected_conditions as EC
class Basepage(object):
    def __init__(self,driver):
        self.driver = driver
    #查找元素
    def find_element(self,locator):

        key = locator.split('**')[0]
        value = locator.split('**')[1]
        if key == 'id':
            WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_id(value).is_displayed())
            return self.driver.find_element_by_id(value)
        if key == 'name':
            WebDriverWait(self.driver, 15).until(lambda the_driver: the_driver.find_element_by_class_name(value).is_displayed())
            return self.driver.find_element_by_class_name(value)
        if key == 'xpath':
            WebDriverWait(self.driver, 5).until(lambda the_driver: the_driver.find_element_by_xpath(value).is_displayed())
            return self.driver.find_element_by_xpath(value)
        if key == 'text':
            WebDriverWait(self.driver, 30).until(lambda the_driver: the_driver.find_element_by_name(value).is_displayed())
            return self.driver.find_element_by_name(value)

    #获取屏幕分辨率
    #def getSize(self):
        #width = self.driver.get_window_size()["width"]
        #height = self.driver.get_window_size()["height"]
        #return (width, height)

