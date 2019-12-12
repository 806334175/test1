#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def get_pm_list(package):
    cmd = "adb shell pm path " + package
    res_path = os.popen(cmd)
    res_path_list = str.split(res_path.read().replace("\n", ""), "package:")
    return res_path_list


def pull_apk(phone_path, pc_path):
    cmd = "adb pull " + phone_path + " " + pc_path
    res_pull = os.popen(cmd)
    print(res_pull.read())
    return res_pull


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
    package = "com.mover.lznh"
    pc_path = "D:\\GoogleAPK\\" + package

    mkdir(pc_path)

    phone_path_list = get_pm_list(package)
    print(phone_path_list)
    for i in range(len(phone_path_list) - 1):
        pull_apk(phone_path_list[i + 1], pc_path)
