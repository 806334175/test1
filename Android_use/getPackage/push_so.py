#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


def install_apk(apk_path):
    cmd = "adb install -r " + apk_path
    print(cmd)
    res = os.popen(cmd)
    print(res.read())
    return res


def check_apk(package):
    cmd = "adb shell pm list packages"
    print(cmd)
    time.sleep(5)
    res = os.popen(cmd)
    return package in res.read()


def get_push_path(package):
    cmd = "adb shell pm path " + package
    print(cmd)
    res_path = os.popen(cmd)
    res_path_list = str.split(res_path.read().replace("\n", ""), "package:")
    res = res_path_list[1].split("base.apk")
    return res[0]


def push_so_file(so_path, push_path):
    cmd = "adb push " + so_path + " " + push_path + "lib/"
    print(cmd)
    res = os.popen(cmd)
    print(res.read())
    return res


def get_file_name(push_path):
    cmd = "adb shell ls " + push_path + "lib/"
    print(cmd)
    res = os.popen(cmd.replace("\n", ""))
    return res.read()


def change_file_name(push_path, old_file_name, new_file_name):
    cmd = "adb shell mv " + push_path + "lib/" + old_file_name + " " + push_path + "lib/" + new_file_name
    print(cmd)
    res = os.popen(cmd.replace("\n", ""))
    print(res.read())
    return res


if __name__ == "__main__":
    package = "com.taobao.tmoversea.android"
    apk_path = "D:\\GoogleAPK\\" + package + "\\base.apk"
    so_path = "D:\\GoogleAPK\\" + package + "\\split_config.armeabi_v7a\\lib"
    new_file_name = "arm"
    # print(check_apk(package))

    # install_apk(apk_path)
    # while True:
    #     if check_apk(package):
    #         break
    #     else:
    #         continue
    push_path = get_push_path(package)
    push_so_file(so_path, push_path)
    old_file_name = get_file_name(push_path)
    change_file_name(push_path, old_file_name, new_file_name)

# cmd = "adb shell mv /data/app/jp.co.cybird.appli.android.gen.ja-n4cnhhkeD0mBw0f8rVP4Gw==/lib/armeabi-v7a /data/app/jp.co.cybird.appli.android.gen.ja-n4cnhhkeD0mBw0f8rVP4Gw==/lib/arm"
# res = os.popen(cmd)
# print(res.read())
