from appium import webdriver
from Common.config import *

kuaishou = devices_message()
class kuaishoudriver:
    def ks_driver(self):
        desired_caps = kuaishou
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)