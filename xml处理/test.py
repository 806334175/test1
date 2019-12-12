#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time

import xmltodict
import json


def load_json(xml_path):
    # 获取xml文件
    xml_file = open(xml_path, 'r', encoding="utf-8")
    # 读取xml文件内容
    xml_str = xml_file.read()
    # 将读取的xml内容转为json
    json1 = xmltodict.parse(xml_str, encoding="utf-8")
    jsonStr = json.dumps(json1, indent=4)
    f = open('json', 'w')
    f.write(jsonStr)
    f.close()
    return jsonStr


# file = open("ttt.TW_xml_file", "r", encoding="utf-8")
# print(file.read())
# print(load_json("ttt.TW_xml_file"))

# load_json("ttt.TW_xml_file")

import xml.etree.ElementTree as ET


def xmlTOsjon(file, name):
    tree = ET.parse(file)
    root = tree.getroot()
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

    ua = dic["web_useragent"]
    myres = re.findall("Android (\d).", ua)
    nn = int(myres[0])
    if nn > 5:
        jsonStr = json.dumps(dic, indent=4)
        f = open("HK_json_file/" + name + '.txt', 'w')
        f.write(jsonStr.strip())
        f.close()


file = open("hk100.xml", "r", encoding="utf-8")
xml_info = file.read()
xml_info_list = xml_info.split("</phones>")

list_xml_info = []

for info in xml_info_list:
    list_xml_info.append(info + "</phones>")

num = 0
for a in list_xml_info:
    num += 1

for i in range(num - 1):
    # f = open("HK_xml_file/" + str(i) + ".xml", "w", encoding="utf-8")
    # f.write(list_xml_info[i].strip())
    # time.sleep(100)
    xmlTOsjon("KR_xml_file/" + str(i) + ".xml", str(i))
