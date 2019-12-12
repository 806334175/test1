#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import json

tree = ET.parse("ttt.TW_xml_file")
root = tree.getroot()

print(root)

list_key = []
list_value = []

for i in root:
    list_key.append(i.attrib["key"])
    list_value.append(i.attrib["value"])

dic = {}
num = 0
for i in list_key:
    dic[list_key[num]] = list_value[num]
    num += 1


jsonStr = json.dumps(dic, indent=4)
print(jsonStr)
f = open('deviceInfo.txt', 'w')
f.write(jsonStr)
f.close()

