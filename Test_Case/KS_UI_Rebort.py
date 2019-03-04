# coding=utf-8
import unittest
from PageObjects.login_ele import Login
from Common.driver import kuaishoudriver
import time
from PageObjects.shouhongbao_ele import Shouhongbao


class Test_KSHB(unittest.TestCase):
    driver = kuaishoudriver().ks_driver()
    phone = 13066909086
    password = 199308


    def test_01_allow(self):
        a =Login(self)
        a.always_allow()

    def test_02_swipeLeft(self):
        a = Login(self)
        a.getSize()
        a.swipeLeft()

    def test_03_login(self):
        a = Login(self.driver)
        a.login(self.phone,self.password)

if __name__ == '__main__':
    unittest.main()