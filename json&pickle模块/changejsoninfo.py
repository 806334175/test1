#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

path = "C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\\deviceInfo.txt"

file = open(path,"r")

a = "TW"
b = "46601"
c = "FarEasTone"

res = json.loads(file.read())
file.close()

res["tele_getnetworkcountryiso"] = a
res["tele_getsimcountryiso"] = a
res["tele_getnetworkoperator"] = b
res["tele_getsimoperator"] = b
res["tele_getsimoperatorname"] = c
res["tele_getnetworkoperatorname"] = c

file = open(path,"w")
j = json.dumps(res)

file.write(j)
