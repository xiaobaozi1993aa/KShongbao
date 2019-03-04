from Common.get_phone import *

a = (readDevicesList()[0])
b = readDevices_version().strip("\n")

def devices_message():
    kuaishou = {
                    'platformName': 'Android',
                    'deviceName': '%s' % a,
                    'platformVersion': '%s' % b,
                    #'app': APP,#PATH('app-release.apk'),
                    'appPackage': 'com.guochuang.mimedia',
                    'appActivity': 'com.guochuang.mimedia.ui.activity.WelcomeActivity',
                    #'appPackage':'io.appium.settings',
                    #'appActivity':'io.appium.settings.Settings',
                    #'noReset': 'true',
                    'resetKeyboard': 'True',                      # 隐藏小键盘
                    'unicodeKeyboard': 'True',                # Unicode编码
                    'autoGrantPermissions':'True'
                    }
    return kuaishou


if __name__ == '__main__':
    print(devices_message())