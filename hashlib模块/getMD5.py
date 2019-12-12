#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def getmd5(file_name):
    m = hashlib.md5()
    file = open(file_name, "rb")
    m.update(file.read())
    return m.hexdigest()


print(getmd5("base.apk"))
# print(getmd5("Xross Chronicle-1.020191017.apk"))
# print(getmd5("com.linegames.xc.apk"))
# print(getmd5("Xross Chronicle-1.0.apk"))
print(getmd5("a.apk"))
