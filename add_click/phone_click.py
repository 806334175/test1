import os
import random
import socket
import urllib
import requests
import rule as rule
import xlwt
import xlrd

import threading
import re

import time, datetime
from xlutils import copy

file = "D:\\offer_track_test.xls"
url_count = 0


def get_lum_ip(track_url, super_proxy_url):
    # get_redirect_url("http://lumtest.com/myip.json", super_proxy_url,d_type)

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
        # 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    }

    proxies = {"http": super_proxy_url,
               "https": super_proxy_url,
               }

    try:
        res = requests.get(track_url, proxies=proxies, headers=headers, allow_redirects=False, timeout=20)
        # print("lum--------------------", res.text)
        if res.text.find("Error") > -1:
            print(res.text)
            return False
        else:
            print(res.text)
            return True
    except requests.exceptions.ProxyError as requestsE:
        # print(requestsE)
        return None
    except  urllib.error.URLError as  requestsE:
        # print(requestsE)
        return None
    except requests.exceptions.RequestException as requestsE:
        # print(requestsE)
        return None
        pass
    pass


def get_redirect_url(track_url, super_proxy_url, ua):
    time.sleep(0.1)
    global url_count
    url_count += 1
    # #print("url跳转的次数%d"%(url_count))

    # #print("get_redirect_url")
    # 重定向前的链接
    res = ""
    rs = ""

    # ua_and = {
    #     # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    #     'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    # }
    # ua_and["User-Agent"]=ua()

    headers = ua
    # print(headers)
    proxies = {
        "http": super_proxy_url,
        "https": super_proxy_url,
    }
    try:
        res = requests.get(track_url, proxies=proxies, headers=headers, allow_redirects=False, timeout=20)
        # print(res.text)
        # print(res.status_code)
    except requests.exceptions.ProxyError as requestsE:
        # print(requestsE)
        return None
    except  urllib.error.URLError as  requestsE:
        # print(requestsE)
        return None
    except requests.exceptions.RequestException as requestsE:
        # print(requestsE)
        return None
        pass

    if type(res) is str:

        return res
        pass
    else:
        if res.status_code == 302:
            res.close()
            # print(res.headers["Location"])
            return res.headers["Location"]

        elif res.status_code == 200:
            # print("200跳")
            if res.text.find("document.location.href") > -1:
                # print("document.location.href")

                aa = re.findall(" = '(.*)';", res.text)[0]
                # print("____________________", aa)
                if aa == "" or aa == None:
                    return res.text
                else:
                    return aa
            elif res.text.find("window.location.replace") > -1:
                aa = re.findall("replace\('(.*)'", res.text)[0]
                # print("____________________", aa)
                if aa == "" or aa == None:
                    return res.text
                else:
                    return aa
            elif res.text.find("http-equiv='refresh'") > -1 and res.text.find("window.location.replace") == -1:
                aa = re.findall("; url=(.*)'>", res.text)[0]
                # print("____________________", aa)
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


def offer_test(track_url, area, device_type):
    appid = "123123123"
    ua_ = {
        # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    }
    ua_["User-Agent"] = ua(device_type)
    # print("track=" + track_url + "  area=" + area + "   appid=" + appid + "  d_type=" + d_type)
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
        # print(track_url)
        try:
            if lum_code == 1:
                res = "Lum错误"
                break
            pass

            if track_url.find('www.google123.com') > -1:
                # print("跳google")
                # print("country:%s--track_link:%s--app_id:%s--失败" % (area, track_url2, appid))
                res = "失败"
                break

            if track_url.find('ttp') > -1 and track_url.find('apple.com') == -1 and track_url.find(
                    'app.appsflyer.com/id') == -1 and track_url.find("details?id") == -1:
                # print("继续跳", track_url)
                track_url = get_redirect_url(track_url, super_proxy_url, ua_)
            elif track_url.find("document.location.href") > -1:
                # print("改改改")
                pass
            else:
                # print("开始判断")
                if track_url.find(appid) > -1:
                    # print("country:%s--track_link:%s--app_id:%s--成功" % (area, track_url2, appid))
                    res = "成功"
                    break
                else:
                    # print("country:%s--track_link:%s--app_id:%s--失败" % (area, track_url2, appid))
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


def ua(device_type):
    # AOSP
    if device_type == "ios":
        WebKit_versin = ('60%d.%d.%d' % (random.randint(4, 5), random.randint(1, 5), random.randint(1, 15)))
        devType = 'iPhone'
        devType2 = ' iPhone'

        datas = data[random.randint(0, 34)]
        datas = str.split(datas, "----")

        dev_version = datas[0]
        web_version = datas[1]
        os_version = datas[2]
        d_version = datas[3].replace('\n', "")
        safari = '604.1'
        # print(devType)
        # print(devType2)
        # print(dev_version)
        # print(WebKit_versin)
        # print(web_version)
        # print(d_version)

        # Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C114 Safari/604.1
        #     super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
        #                        (username, area, session_id, password, port))
        ios_ua = (
                'Mozilla/5.0 (%s; CPU%s OS %s like Mac OS X) AppleWebKit/%s (KHTML, like Gecko) Version/%s Mobile/%s Safari/%s'
                % (devType, devType2, dev_version, WebKit_versin, web_version, d_version, safari))

        print(ios_ua)
        return ios_ua
    elif device_type == "and":
        ua_head = devices_build[random.randint(1, 15540)]
        chrome_v = ["77", "76", "75", "74", "73", "72", "71", "70", "69", "68", "67", "66", "65"]
        safari_v = ["537.36", "530.17", "534.13", "534.30", "535.19", "533.1"]
        chrome_v2 = int(random.randint(1111, 2000))
        chrome_v3 = random.randint(1, 150)
        # Mozilla/5.0 (Linux; Android 6.0; AOSP on Shamu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36
        and_ua = ('%s Chrome/%s.0.%s.%s Mobile Safari/%s') % (
            ua_head, chrome_v[random.randint(1, 12)], chrome_v2, chrome_v3, safari_v[random.randint(1, 5)])
        and_ua = and_ua.replace('\n', "")
        print(and_ua)
        return and_ua
    else:
        print("ua错误——————————————————————————————————————————————")

    # Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36


# # Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C114 Safari/604.1
# #     super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
# #                        (username, area, session_id, password, port))

#     print(ios_ua )
#     return ios_ua


def test_url(track, country, device_type, click_count, speed):
    # for cols in range(2):
    for num in range(click_count):
        print("当前任务-", track, "-", country, "-", click_count, "=", num)
        threading.Thread(target=offer_test, args=(track, country, device_type)).start()
        time.sleep(60 / speed)
    pass
    print("任务完成", track, country, click_count)


if __name__ == '__main__':
    e = open("ua.txt", "r")
    data = e.readlines()
    e.close()
    f = open("device_build.txt", "r")
    devices_build = f.readlines()
    f.close()

    list = []

    # mobikok_KR_carplat = ["http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96550387", "KR", "and", 300, 5]
    # yeahmobi_HK_rlwj = ["http://global.ymtracking.com/trace?offer_id=19094510&aff_id=111819", "HK", "and", 2000, 50]
    yeahmobi_HK_rlwj = ["http://clkbb.tbnetwork.im/click?id=7240696&aff=555&ost=1575535139", "TW", "and", 1000, 50]


    # list.append(mobikok_KR_carplat)
    list.append(yeahmobi_HK_rlwj)
    for i in range(len(list)):
        threading.Thread(target=test_url, args=(list[i][0], list[i][1], list[i][2], list[i][3], list[i][4])).start()
