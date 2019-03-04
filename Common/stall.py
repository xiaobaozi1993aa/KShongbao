import os
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.driver import kuaishoudriver
import time

#def adb_install():
   # os.system('adb install app-release.apk')
driver = kuaishoudriver().ks_driver()

#com.guochuang.mimedia:id/tv_guide_into 引导页
#com.guochuang.mimedia:id/et_login_phone 名字
#com.guochuang.mimedia:id/et_login_password 密码
def always_allow(driver,number = 30):
    for i in range(number):
        loc = ("xpath", "//*[@text='允许']")
        try:
            e = WebDriverWait(driver,1,0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            print('找不到该元素')

#获取屏幕宽度和高度
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
#向左滑动
def swipeLeft():
    l = getSize()
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1)
    driver.swipe(x1, y1, x2, y1)
    driver.find_element_by_id('com.guochuang.mimedia:id/tv_guide_into').click()

def login():
    driver.find_element_by_id('com.guochuang.mimedia:id/et_login_phone').send_keys('13066909086')
    driver.find_element_by_id('com.guochuang.mimedia:id/et_login_password').send_keys('199308')
    driver.close_app()
threads = []
t1 = threading.Thread(target=always_allow)
threads.append(t1)

if __name__ == '__main__':

    for t in threads:
        t.setDeamon(True)
        t.start()
    getSize()
    swipeLeft()
    login()

