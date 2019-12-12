#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def pushfile():
    cmd1 = "adb shell mkdir /sdcard/abc"
    cmd2 = "adb shell mkdir /sdcard/script"
    cmd3 = "adb push engine.js /sdcard/script/"
    cmd4 = "adb push ip_mode.txt /sdcard/script/"
    cmd5 = "adb push PC_lum_hostandport.txt /sdcard/script/"
    cmd6 = "adb push IP_state.txt /sdcard/script/"
    cmd7 = "adb push package_now.txt /sdcard/script/"
    cmd8 = "adb push PC_hostandport.txt /sdcard/script/"
    cmd9 = "adb push phone_prot.txt /sdcard/script/"
    cmd10 = "adb push utils.js /sdcard/script/"
    cmd11 = "adb push get_Jurisdiction.js /sdcard/script/"
    cmd12 = "adb push use_911.js /sdcard/script/"
    cmd13 = "adb push use_lum.js /sdcard/script/"
    cmd14 = "adb push open_root.js /sdcard/script/"

    # p1 = os.popen(cmd1)
    # p1.close()
    # p2 = os.popen(cmd2)
    # p2.close()
    # p3 = os.popen(cmd3)
    # p3.close()
    # p4 = os.popen(cmd4)
    # p4.close()
    # p5 = os.popen(cmd5)
    # p5.close()
    # p6 = os.popen(cmd6)
    # p6.close()
    # p7 = os.popen(cmd7)
    # p7.close()
    # p8 = os.popen(cmd8)
    # p8.close()
    # p9 = os.popen(cmd9)
    # p9.close()
    p10 = os.popen(cmd10)
    p10.close()
    # p11 = os.popen(cmd11)
    # p11.close()
    # p12 = os.popen(cmd12)
    # p12.close()
    # p13 = os.popen(cmd13)
    # p13.close()
    # p14 = os.popen(cmd14)
    # p14.close()


def installpackage():
    cmd14 = "adb install base.apk"
    cmd15 = "adb install proxy.apk"
    cmd16 = "adb install script_engine_v1.0.1.apk"
    cmd17 = "adb install jump20191204.apk"
    # cmd18 = "adb install asharedolls.apk"
    # cmd18 = "adb install com.tw.king.apk"

    # p18 = os.popen(cmd18)
    # p18.close()
    p14 = os.popen(cmd14)
    p14.close()
    p15 = os.popen(cmd15)
    p15.close()
    p16 = os.popen(cmd16)
    p16.close()
    p17 = os.popen(cmd17)
    p17.close()



def changefile(host, prot):
    file1 = open("PC_hostandport.txt", "w")
    file2 = open("PC_lum_hostandport.txt", "w")
    file3 = open("phone_prot.txt", "w")

    file1.write(host + "-10088")
    file2.write(host + "-" + prot)
    file3.write(prot)

    file1.close()
    file2.close()
    file3.close()

    pass


if __name__ == '__main__':
    # prot = "5000"
    #
    # host = "192.168.112.69"
    #
    # print(host+"---"+prot)
    # changefile(host, prot)
    pushfile()
    installpackage()
