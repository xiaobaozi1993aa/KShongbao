import os
def readDevicesList():
    p = os.popen('adb devices')
    devicesList = p.read()
    p.close()
    lists = devicesList.split("\n")
    devicesNames = []
    for item in lists:
        if (item.strip() == ""):
            continue
        elif (item.startswith("List of")):
            continue
        else:
            devicesNames.append(item.split("\t")[0])
    return devicesNames

def readDevices_version():
    p = os.popen('adb shell getprop ro.build.version.release')
    version = p.read()
    p.close()
    return version

if __name__ == '__main__':
    print((readDevicesList())[0])
    print(readDevices_version())
