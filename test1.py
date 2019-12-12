# num = 10
#
#
# def demo1():
#     a = 11
#     b = 22
#     return a, b
#
#
# def demo2():
#     a = 1
#     b = 2
#
#     [a, b] = [b, a]
#     print(a)
#     print(b)
#     pass
#
#
# def demo3(num_list):
#     num_list.clear()
#     num_list.append("123")
#     num_list.append("456")
#     pass
#
#
# gl_list = [1, 2, 3]
# demo3(gl_list)
# print(gl_list)
#
# str = "  a  b   c   "
# print(str)
# print(str.strip())
# print(str.replace(" ", ""))


# class Sample:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, type, value, trace):
#         print
#         "type:", type
#         print
#         "value:", value
#         print
#         "trace:", trace
#
#     def do_something(self):
#         bar = 1 / 0
#         return bar + 10
#
#
# with Sample() as sample:
#     sample.do_something()


#

import os
import json

# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         print(root)  # 当前目录路径
#         print(dirs)  # 当前路径下所有子目录
#         print(files)  # 当前路径下所有非目录子文件
#
#     for i in files:
#         print(i)
#
#
# file_name("C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\\安卓测试包20191010")


# import re
#
# a = '<meta http-equiv="refresh" content="0; url=http://cd-down.com?a=90483&c=203256&oc=93667&sr=t&s1=216701_555&s2=201910211619395222855065700971791&vt=1571645983471&h=f4a9bfb17142e89be03d13a2c85cbaabf335ef04&req=http%3A%2F%2Fcd-down.com%2F%3Fa%3D90483%26c%3D203256%26s1%3D216701_555%26s2%3D201910211619395222855065700971791%26s3%3D%26s4%3D&us=00000000000000000000000000000000"/>'
# b = "asd123asd456asd786f"
# print(re.findall("(sd|56a).*(a|f)", b))

import os
import re

adb = "ls -al /data/data/"
cmd = 'adb shell su -c "%s"' % adb

res = os.popen(cmd)

mystr = res.read()
print(mystr)
a = str.split(mystr, "\n")

for i in a:
    ress = re.findall(".*com.android.calculator2$", i)
    if len(ress) == 0:
        continue
    else:
        print(ress[0][15:25].replace(" ", ""))




