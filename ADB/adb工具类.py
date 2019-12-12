#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
adb 工具类
"""

import os
import platform
import re
import time


class AdbTools(object):

    def __init__(self, device_id=""):
        self.__device_id = device_id

    def set_device_id(self, args):
        self.__device_id = str(args)

    def cmd(self, args):
        return os.popen(str(args)).read()

    def get_devices(self):
        devices = self.cmd("adb devices")
        devices_list = str.split(devices, "\n")
        list_device = []
        for i in range(len(devices_list) - 2):
            if i == 0:
                continue
            else:
                if devices_list[i][11:17] == "device":
                    list_device.append(devices_list[i][0:10])
        if len(list_device) < 1:
            return False
        else:
            return list_device

    def ADB(self, args):
        res = self.cmd('adb -s %s shell "%s"' % (str(self.__device_id), str(args)))
        return res

    def su_ADB(self, args):
        res = self.cmd('adb -s %s shell su -c "%s"' % (str(self.__device_id), str(args)))
        return res

    def get_launcher_activity(self, package):
        res = self.ADB("dumpsys package %s" % package)
        res_list = re.findall("(" + package + ".*) filter", res)
        print(res_list)
        return res_list

    def start_activity(self, args):
        activity = self.get_launcher_activity(args)
        res = self.ADB("am start -n %s" % str(activity[1]))
        return res

    def swipe(self, x1, y1, x2, y2):
        res = self.ADB("input swipe %s %s %s %s" % (str(x1), str(y1), str(x2), str(y2)))
        return res

    def keyevent(self, args):
        res = self.ADB("input keyevent %s" % str(args))
        return res

    def inputtext(self, args):
        res = self.ADB('input text "%s"' % str(args))
        return res

    def tap(self, x, y):
        res = self.ADB('input tap %s %s' % (str(x), str(y)))
        return res


class KeyCode:
    KEYCODE_CALL = 5  # 拨号键
    KEYCODE_ENDCALL = 6  # 挂机键
    KEYCODE_HOME = 3  # Home键
    KEYCODE_MENU = 82  # 菜单键
    KEYCODE_BACK = 4  # 返回键
    KEYCODE_SEARCH = 84  # 搜索键
    KEYCODE_CAMERA = 27  # 拍照键
    KEYCODE_FOCUS = 80  # 对焦键
    KEYCODE_POWER = 26  # 电源键
    KEYCODE_NOTIFICATION = 83  # 通知键
    KEYCODE_MUTE = 91  # 话筒静音键
    KEYCODE_VOLUME_MUTE = 164  # 扬声器静音键
    KEYCODE_VOLUME_UP = 24  # 音量+键
    KEYCODE_VOLUME_DOWN = 25  # 音量-键
    KEYCODE_ENTER = 66  # 回车键
    KEYCODE_ESCAPE = 111  # ESC键
    KEYCODE_DPAD_CENTER = 23  # 导航键 >> 确定键
    KEYCODE_DPAD_UP = 19  # 导航键 >> 向上
    KEYCODE_DPAD_DOWN = 20  # 导航键 >> 向下
    KEYCODE_DPAD_LEFT = 21  # 导航键 >> 向左
    KEYCODE_DPAD_RIGHT = 22  # 导航键 >> 向右
    KEYCODE_MOVE_HOME = 122  # 光标移动到开始键
    KEYCODE_MOVE_END = 123  # 光标移动到末尾键
    KEYCODE_PAGE_UP = 92  # 向上翻页键
    KEYCODE_PAGE_DOWN = 93  # 向下翻页键
    KEYCODE_DEL = 67  # 退格键
    KEYCODE_FORWARD_DEL = 112  # 删除键
    KEYCODE_INSERT = 124  # 插入键
    KEYCODE_TAB = 61  # Tab键
    KEYCODE_NUM_LOCK = 143  # 小键盘锁
    KEYCODE_CAPS_LOCK = 115  # 大写锁定键
    KEYCODE_BREAK = 121  # Break / Pause键
    KEYCODE_SCROLL_LOCK = 116  # 滚动锁定键
    KEYCODE_ZOOM_IN = 168  # 放大键
    KEYCODE_ZOOM_OUT = 169  # 缩小键
    KEYCODE_0 = 7
    KEYCODE_1 = 8
    KEYCODE_2 = 9
    KEYCODE_3 = 10
    KEYCODE_4 = 11
    KEYCODE_5 = 12
    KEYCODE_6 = 13
    KEYCODE_7 = 14
    KEYCODE_8 = 15
    KEYCODE_9 = 16
    KEYCODE_A = 29
    KEYCODE_B = 30
    KEYCODE_C = 31
    KEYCODE_D = 32
    KEYCODE_E = 33
    KEYCODE_F = 34
    KEYCODE_G = 35
    KEYCODE_H = 36
    KEYCODE_I = 37
    KEYCODE_J = 38
    KEYCODE_K = 39
    KEYCODE_L = 40
    KEYCODE_M = 41
    KEYCODE_N = 42
    KEYCODE_O = 43
    KEYCODE_P = 44
    KEYCODE_Q = 45
    KEYCODE_R = 46
    KEYCODE_S = 47
    KEYCODE_T = 48
    KEYCODE_U = 49
    KEYCODE_V = 50
    KEYCODE_W = 51
    KEYCODE_X = 52
    KEYCODE_Y = 53
    KEYCODE_Z = 54
    KEYCODE_PLUS = 81  # +
    KEYCODE_MINUS = 69  # -
    KEYCODE_STAR = 17  # *
    KEYCODE_SLASH = 76  # /
    KEYCODE_EQUALS = 70  # =
    KEYCODE_AT = 77  # @
    KEYCODE_POUND = 18  # #
    KEYCODE_APOSTROPHE = 75  # '
    KEYCODE_BACKSLASH = 73  # \
    KEYCODE_COMMA = 55  # ,
    KEYCODE_PERIOD = 56  # .
    KEYCODE_LEFT_BRACKET = 71  # [
    KEYCODE_RIGHT_BRACKET = 72  # ]
    KEYCODE_SEMICOLON = 74  # ;
    KEYCODE_GRAVE = 68  # `
    KEYCODE_SPACE = 62  # 空格键
    KEYCODE_MEDIA_PLAY = 126  # 多媒体键 >> 播放
    KEYCODE_MEDIA_STOP = 86  # 多媒体键 >> 停止
    KEYCODE_MEDIA_PAUSE = 127  # 多媒体键 >> 暂停
    KEYCODE_MEDIA_PLAY_PAUSE = 85  # 多媒体键 >> 播放 / 暂停
    KEYCODE_MEDIA_FAST_FORWARD = 90  # 多媒体键 >> 快进
    KEYCODE_MEDIA_REWIND = 89  # 多媒体键 >> 快退
    KEYCODE_MEDIA_NEXT = 87  # 多媒体键 >> 下一首
    KEYCODE_MEDIA_PREVIOUS = 88  # 多媒体键 >> 上一首
    KEYCODE_MEDIA_CLOSE = 128  # 多媒体键 >> 关闭
    KEYCODE_MEDIA_EJECT = 129  # 多媒体键 >> 弹出
    KEYCODE_MEDIA_RECORD = 130  # 多媒体键 >> 录音


if __name__ == '__main__':
    at = AdbTools()
    list_device = at.get_devices()
    at.set_device_id(list_device[0])
    # print(at.su_ADB("ls -al /data/data/"))
    # print(at.ADB("pm list packages -3"))
    # at.start_activity("com.touchsprite.android")
    # at.swipe(100,600,100,900)
    # at.keyevent(KeyCode.KEYCODE_HOME)
    while True:
        at.tap(821,560)
        print(time.time())
    pass
