#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

        return files


def install(file_dir, filename):
    cmd = "adb install " + file_dir + "\\" + filename
    p1 = os.popen(cmd)
    print(filename + ":" + p1.read())
    p1.close()


if __name__ == "__main__":
    path = "C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\安卓API任务\\apk_download\\KR"
    apkname_list = file_name(path)
    for i in range(len(apkname_list) - 1):
        print("第" + str(i + 1) + "个")
        installname = apkname_list[i]
        if installname.find("v8a") == -1:
            if installname.find(".obb") == -1:
                if installname.find(".crdownload") == -1:
                    install(path, installname)
