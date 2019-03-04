import unittest
from Test_Case.KS_UI_Rebort import Test_KSHB
from lib import HTMLTestRunner
import time
import threading
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.driver import kuaishoudriver



def kshb_report():              #用例执行加生成报告
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_KSHB)          #用例添加
    now = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime())           #时间字符串
    report_path = 'C:\\Users\\Administrator\\PycharmProjects\\KShongbao\\KS_Report\\'+now+'_report.html'        #报告路径
    fp  = open(report_path,'wb')        #打开文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="快收测试报告",description='回归测试如下：')      #执行
    runner.run(suite)
    fp.close()



if __name__ == '__main__':
    kshb_report()
