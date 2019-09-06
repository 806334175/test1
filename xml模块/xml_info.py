#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print('========>', child.tag, child.attrib, child.attrib['name'])
    for i in child:
        print(i.tag, i.attrib, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)






# ---------------------------------------
# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
#
# # 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set('updated', 'yes')
#     node.set('version', '1.0')
# tree.write('test.xml')
#
# # 删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')