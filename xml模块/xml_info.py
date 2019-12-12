#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----查询----------------------------------------
# import TW_xml_file.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.TW_xml_file")
# root = tree.getroot()
# print(root.tag)
#
# # 遍历xml文档
# for child in root:
#     print('========>', child.tag, child.attrib, child.attrib['name'])
#     for i in child:
#         print(i.tag, i.attrib, i.text)
#
# # 只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag, node.text)

# ----修改删除-----------------------------------
# import TW_xml_file.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.TW_xml_file")
# root = tree.getroot()
#
# # 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set('updated', 'yes')
#     node.set('version', '1.0')
# tree.write('test.TW_xml_file')
#
# # 删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.TW_xml_file')


# ----增加----------------------------------------
# 在country内添加（append）节点year2
# import TW_xml_file.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.TW_xml_file")
# root = tree.getroot()
# for country in root.findall('country'):
#     for year in country.findall('year'):
#         if int(year.text) > 2000:
#             year2 = ET.Element('year2')
#             year2.text = '新年'
#             year2.attrib = {'update': 'yes'}
#             country.append(year2)  # 往country节点下添加子节点
#
# tree.write('a.TW_xml_file.swap')

# ----创建------------------------------
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.TW_xml_file", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式