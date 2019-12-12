#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

file = open("YOUAPP.txt","r")

res = json.loads(file.read())
data = res["data"]

list_name = []
list_track = []
list_preview_url = []
list_package = []
list_country = []

for i in data:
    list_country.append(i["countries"])
    list_name.append(i["app_name"])
    list_track.append(i["click_url"])
    list_preview_url.append(i["preview_url"])
    list_package.append(i["app_pack_name"])




for x in list_package:
    print(x)