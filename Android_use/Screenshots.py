#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time


def start_Screenshots(name):
    cmd = "adb shell screencap -p /sdcard/" + name + ".png"
    print(cmd)
    res = os.popen(cmd)
    print(res.read())
    pass


def pull_Screenshots(name, path):
    cmd = "adb pull /sdcard/" + name + ".png " + path
    print(cmd)
    res = os.popen(cmd)
    print(res.read())
    cmd2 = "adb shell rm /sdcard/" + name + ".png"
    print(cmd2)
    res2 = os.popen(cmd2)
    print(res2.read())
    pass


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


if __name__ == "__main__":
    name = time.strftime("%Y%m%d%H%M%S")
    mkdir("C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\\Screenshots\\" + time.strftime("%Y%m%d"))
    path = "C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\\Screenshots\\" + time.strftime(
        "%Y%m%d") + "\\" + name + ".png"
    start_Screenshots(name)
    pull_Screenshots(name, path)
    pass
