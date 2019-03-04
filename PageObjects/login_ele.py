from Common.Basepage import Basepage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.driver import kuaishoudriver

driver = kuaishoudriver().ks_driver()

class Login(Basepage):

    weixin_login = 'text**手机登录'
    phone_number = 'id**com.guochuang.mimedia:id/et_login_phone'
    password_id = 'id**com.guochuang.mimedia:id/et_login_password'
    phone_login_id = 'id**com.guochuang.mimedia:id/et_login_phone'
    guidance_id = 'id**com.guochuang.mimedia:id/tv_guide_into'


    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)
    #引导页滑动
    def swipeLeft(self):
        l = Login.getSize(self)
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1)
        self.driver.swipe(x1, y1, x2, y1)
        self.find_element(self.guidance_id).click()

    def always_allow(driver, number=5):
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                print('找不到该元素')
    #手机登录
    def login(self,phone,password):
        self.find_element(self.phone_number).send_keys(phone)
        self.find_element(self.password_id).send_keys(password)
        self.find_element(self.phone_login_id).click()


    #微信登录
    #def personal(self):
        #self.find_element(self.phone_weixin_login).click()


if __name__ == '__main__':
    a = Login(Basepage)
    a.always_allow()
    time.sleep(5)

    a.getSize()
    a.swipeLeft()
    a.login(13066909086,199308)

