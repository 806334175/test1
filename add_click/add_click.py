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
        # print('except:', e)
        # print("读取列为空")
        return 0
    except PermissionError as e:
        # print('except:', e)
        # print("excel文件没有关闭")
        return 0
    return cols_res


def read_cols_excel(sheet, cols):
    try:
        wb = xlrd.open_workbook(filename=file)
        sheet1 = wb.sheet_by_index(sheet)
        cols_res = sheet1.col_values(cols)
    except IndexError as e:
        # print('except:', e)
        # print("读取列为空")
        return 0
    except PermissionError as e:
        # print('except:', e)
        # print("excel文件没有关闭")
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
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }

    proxies = {"http": super_proxy_url,
               "https": super_proxy_url,
               }

    try:
        res = requests.get(track_url, proxies=proxies, headers=headers, allow_redirects=False, timeout=20)
        if res.text.find("Error") > -1:
            print(res.text)
            return False
        else:
            print(res.text)
            return True
    except requests.exceptions.ProxyError as requestsE:
        return None
    except urllib.error.URLError as requestsE:
        return None
    except requests.exceptions.RequestException as requestsE:
        return None


def get_redirect_url(track_url, super_proxy_url, d_type, my_ua):
    time.sleep(0.1)
    global url_count
    url_count += 1

    ua_ios = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }
    ua_ios["User-Agent"] = my_ua

    ua_and = {
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
    except requests.exceptions.ProxyError as requestsE:
        return None
    except urllib.error.URLError as  requestsE:
        return None
    except requests.exceptions.RequestException as requestsE:
        return None
        pass

    if type(res) is str:
        return res
    else:
        if res.status_code == 302:
            res.close()
            return res.headers["Location"]
        elif res.status_code == 200:
            try:
                if res.text.find("document.location.href") > -1:
                    aa = re.findall(" = '(.*)';", res.text)[0]
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
                else:
                    return res.text
            except  IndexError as  IndexError:
                print(IndexError)
                pass


def offer_test(track_url, area, d_type):
    username = 'lum-customer-yixuanquan-zone-residential-route_err-block'
    password = '7l3viel69de9'
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' % (username, area, session_id, password, port))

    lum_code = 0
    my_ua = ua()

    if (get_lum_ip("http://lumtest.com/myip.json", super_proxy_url)) == False:
        lum_code = 1

    while True:
        try:
            if lum_code == 1:
                break

            if track_url.find('www.google.com') > -1:
                break
            if track_url.find('ttp') > -1 and track_url.find('apple.com') == -1 and track_url.find('app.appsflyer.com/id') == -1 and track_url.find("details?id") == -1:
                track_url = get_redirect_url(track_url, super_proxy_url, d_type, my_ua)
            elif track_url.find("document.location.href") > -1:
                # print("改改改")
                pass
            else:
                # print("开始判断")
                break
        except AttributeError as  e:
            break
        except requests.exceptions.SSLError as  e:
            break
        except requests.exceptions.InvalidSchema as  e:
            break


def ua():
    WebKit_versin = ('60%d.%d.%d' % (random.randint(4, 5), random.randint(1, 5), random.randint(1, 15)))
    devType = 'iPhone'
    devType2 = 'iPhone'

    datas = data[random.randint(0, 46)]
    datas = str.split(datas, "----")

    dev_version = datas[0]
    web_version = datas[1]
    os_version = datas[2]
    d_version = datas[3].replace('\n', "")
    safari = '604.1'
    ios_ua = ('Mozilla/5.0 (%s; CPU%s OS %s like Mac OS X) AppleWebKit/%s (KHTML, like Gecko) Version/%s Mobile/%s Safari/%s' % (
        devType, devType2, dev_version, WebKit_versin, web_version, d_version, safari))

    return ios_ua


pass


def test_url(track, country, d_type, click_count, speed):
    for num in range(click_count):
        print(num)
        threading.Thread(target=offer_test, args=(track, country, d_type,)).start()
        time.sleep(60 / speed)


if __name__ == '__main__':
    data = []
    f = open("ua.txt", "r")
    data = f.readlines()
    f.close()

    # click_count = 4000
    # speed = 100

    offer_list = []
    # TW----------------------------
    # VNSmedia_lznh = ["https://gametraffic.g2afse.com/click?pid=39&offer_id=632&sub2=632&sub4=Nijs.ojj", "TW", "IOS", 2000, 100]
    # TWtb_rlwj = ["http://clkbb.tbnetwork.im/click?id=5100601&aff=555&ost=1572232092&aff_sub=5100610", "TW", "IOS", 2000, 100]
    # lznh = ["http://clkbb.tbnetwork.im/click?id=5040729&aff=555&&aff_sub=5040731", "TW", "IOS", 2000, 100]
    # TWmobpeas_rlwj = ["https://track.mobpeas.com/offer?offer_id=30968119&aff_id=327&aff_pub=30968120", "TW", "IOS", 1500, 9]
    # KR----------------------------
    # mobikok_lznh = ["http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96482362&aff_sub=96482362", "KR", "IOS", 2000, 100]
    # mobisummer_lznh = ["http://click.tracksummer.com/aff_c?offer_id=138331064&affiliate_id=10040&aff_sub5=138331064", "KR", "IOS", 2000, 100]
    # KRmobpeas_lznh = ["https://track.mobpeas.com/offer?offer_id=30968116&aff_id=327&aff_sub=30968116", "KR", "IOS", 2000, 100]
    # KRTB_lznh2 = ["http://clkbb.tbnetwork.im/click?id=4954538&aff=555&ost=1572489600&aff_sub=4954538", "KR", "IOS", 2000, 100]
    # yeahmobi_rz = ["https://global.ymtracking.com/trace?offer_id=19630107&aff_id=111819&sub_affiliate_id=19630107", "KR", "IOS", 2000, 100]

    # HK----------------------------
    # HKTB_rlwj = ["http://clkbb.tbnetwork.im/click?id=5100602&aff=555&ost=1572229263&aff_sub=5100620", "HK", "IOS", 2000, 100]
    # HKTB_lznh = ["http://clkbb.tbnetwork.im/click?id=5051778&aff=555&ost=1572313927&aff_sub=5051780", "HK", "IOS", 2000, 100]
    # yeahmobi_sgsmjz = ["https://global.ymtracking.com/trace?offer_id=19625925&aff_id=111819&sub_affiliate_id=19625926", "HK", "IOS", 5000, 35]

    # VN----------------------------
    # VNyeahmobi_Sendo = ["https://global.ymtracking.com/trace?offer_id=18212459&aff_id=111819&sub_affiliate_id=18212459", "VN", "IOS", 5000, 35]
    Zee5 = ["http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96546959", "IN", "ANDROID", 5000, 35]

    # offer_list.append(VNSmedia_lznh)
    # offer_list.append(TWtb_rlwj)
    # offer_list.append(lznh)
    # offer_list.append(mobikok_lznh)
    # offer_list.append(mobisummer_lznh)
    # offer_list.append(KRmobpeas_lznh)
    # offer_list.append(KRTB_lznh2)
    # offer_list.append(yeahmobi_rz)
    # offer_list.append(HKTB_rlwj)
    # offer_list.append(HKTB_lznh)
    # offer_list.append(TWmobpeas_rlwj)
    # offer_list.append(yeahmobi_sgsmjz)
    # offer_list.append(VNyeahmobi_Sendo)

    for row in range(len(offer_list)):
        threading.Thread(target=test_url, args=(offer_list[row][0], offer_list[row][1], offer_list[row][2], offer_list[row][3], offer_list[row][4],)).start()
        time.sleep(1)
    pass
