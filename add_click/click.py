import os
import random
import socket
import urllib
import requests
import xlwt
import xlrd
import threading
import re
import time
from xlutils import copy

file = "D:\\offer_track_test.xls"
url_count = 0


def read_rows_excel(sheet, row):
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_index(sheet)
    rows_res = sheet1.row_values(row)
    return rows_res


def read_cols_excel(sheet, cols):
    try:
        wb = xlrd.open_workbook(filename=file)
        sheet1 = wb.sheet_by_index(sheet)
        cols_res = sheet1.col_values(cols)
    except IndexError as e:
        #print('except:', e)
        #print("读取列为空")
        return 0
    except PermissionError as e:
        #print('except:', e)
        #print("excel文件没有关闭")
        return 0
    return cols_res


def read_cols_excel(sheet, cols):
    try:
        wb = xlrd.open_workbook(filename=file)
        sheet1 = wb.sheet_by_index(sheet)
        cols_res = sheet1.col_values(cols)
    except IndexError as e:
        #print('except:', e)
        #print("读取列为空")
        return 0
    except PermissionError as e:
        #print('except:', e)
        #print("excel文件没有关闭")
        return 0
    return cols_res


def write_excel(sheet, row, col, str):
    try:
        # mylock.acquire()
        # myfile = open(file)
        # fcntl.flock(myfile.fileno(), fcntl.LOCK_EX)
        rb = xlrd.open_workbook(filename=file)
        wb = copy.copy(rb)
        sheet1 = wb.get_sheet(sheet)
        sheet1.write(row, col, str)
        os.remove(file)
        wb.save(file)
        # mylock.release()
    except IndexError as e:
        return 1
    except xlrd.biffh.XLRDError as e:
        return 1
    except FileNotFoundError as e:
        return 1
    except PermissionError as e:
        return 1
    return 0


def get_lum_ip(track_url, super_proxy_url):
    # get_redirect_url("http://lumtest.com/myip.json", super_proxy_url,d_type)

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
        # 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    }

    proxies = {"http": super_proxy_url,
               "https": super_proxy_url,
               }
    res = requests.get(track_url, proxies=proxies, headers=headers, allow_redirects=False, timeout=20)
    #print("lum--------------------", res.text)
    if res.text.find("Error") > -1:
        print(res.text)
        return False
    else:
        print(res.text)
        return True
    pass


def get_redirect_url(track_url, super_proxy_url, d_type):
    time.sleep(0.1)
    global url_count
    url_count += 1
    # #print("url跳转的次数%d"%(url_count))

    # #print("get_redirect_url")
    # 重定向前的链接
    res = ""
    rs = ""
    ua_ios = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
        # 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    }
    ua_and = {
        # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    }
    if d_type == "IOS":
        headers = ua_ios
    else:
        headers = ua_and

    proxies = {
        "http": super_proxy_url,
        "https": super_proxy_url,
    }
    try:
        res = requests.get(track_url, proxies=proxies, headers=headers, allow_redirects=False, timeout=20)
        #print(res.text)
        #print(res.status_code)
    except requests.exceptions.ProxyError as requestsE:
        #print(requestsE)
        return None
    except  urllib.error.URLError as  requestsE:
        #print(requestsE)
        return None
    except requests.exceptions.RequestException as requestsE:
        #print(requestsE)
        return None
        pass

    if type(res) is str:

        return res
        pass
    else:
        if res.status_code == 302:
            res.close()
            return res.headers["Location"]

        elif res.status_code == 200:
            #print("200跳")
            if res.text.find("document.location.href") > -1:
                #print("document.location.href")

                aa = re.findall(" = '(.*)';", res.text)[0]
                #print("____________________", aa)
                if aa == "" or aa == None:
                    return res.text
                else:
                    return aa
            elif res.text.find("window.location.replace") > -1:
                aa = re.findall("replace\('(.*)'", res.text)[0]
                #print("____________________", aa)
                if aa == "" or aa == None:
                    return res.text
                else:
                    return aa
            elif res.text.find("http-equiv='refresh'") > -1 and res.text.find("window.location.replace") == -1:
                aa = re.findall("; url=(.*)'>", res.text)[0]
                #print("____________________", aa)
                if aa == "" or aa == None:
                    return res.text
                else:
                    return aa


            # elif res.text.find("window.location.href=")>-1:
            #     aa = re.findall("window.location.href='(.*);'", res.text)[0]
            #     #print("____________________", aa)
            #     if aa == "" or aa == None:
            #         return res.text
            #     else:
            #         return aa
            else:
                return res.text


def offer_test(track_url, area, appid, d_type, row, cols):
    #print("track=" + track_url + "  area=" + area + "   appid=" + appid + "  d_type=" + d_type)
    # username = 'lum-customer-hl_f5b348f3-zone-static-route_err-block'
    username = 'lum-customer-yixuanquan-zone-residential-route_err-block'
    password = '7l3viel69de9'
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                       (username, area, session_id, password, port))
    track_url2 = track_url
    lum_code = 0
    res = "失败"
    if (get_lum_ip("http://lumtest.com/myip.json", super_proxy_url)) == False:
        lum_code = 1
    pass
    while True:
        #print(track_url)
        try:
            if lum_code == 1:
                res = "Lum错误"
                break
            pass

            if track_url.find('www.google.com') > -1:
                #print("跳google")
                #print("country:%s--track_link:%s--app_id:%s--失败" % (area, track_url2, appid))
                res = "失败"
                break

            if track_url.find('ttp') > -1 and track_url.find('apple.com') == -1 and track_url.find(
                    'app.appsflyer.com/id') == -1 and track_url.find("details?id") == -1:
                #print("继续跳", track_url)
                track_url = get_redirect_url(track_url, super_proxy_url, d_type)
            elif track_url.find("document.location.href") > -1:
                #print("改改改")
                pass
            else:
                #print("开始判断")
                if track_url.find(appid) > -1:
                    #print("country:%s--track_link:%s--app_id:%s--成功" % (area, track_url2, appid))
                    res = "成功"
                    break
                else:
                    #print("country:%s--track_link:%s--app_id:%s--失败" % (area, track_url2, appid))
                    res = "失败"
                    break
                break

        except AttributeError as  e:
            res = "失败"
            break
            pass
        except requests.exceptions.SSLError as  e:
            res = "失败"
            break
            pass
        except requests.exceptions.InvalidSchema as  e:
            res = "失败"
            break
            pass
    # while True:
    #     if write_excel(0, row, cols + 10, res) == 0:
    #         break
    #     else:
    #         time.sleep(1)
    #         continue


def test_url(track, country, appid, d_type, row):
    # for cols in range(2):
    threading.Thread(target=offer_test, args=(track, country, appid, d_type, row, 0,)).start()



if __name__ == '__main__':
    # list_track = read_cols_excel(0, 8)
    # list_county = read_cols_excel(0, 5)
    # list_appid = read_cols_excel(0, 2)
    # list_d_type = read_cols_excel(0, 6)

    track_url = "http://clkbb.tbnetwork.im/click?id=5100602&aff=555&ost=1572229263"
    county = "HK"
    appid = "1462885516"
    d_type = "IOS"

    row = 0

    for row in range(200):
        row += 1
        threading.Thread(target=test_url,
                         args=(track_url, county, appid, d_type, row,)).start()
        time.sleep(5)
