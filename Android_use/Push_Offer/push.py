#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import requests


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件

        return files[0]


def get_deviceinfo(mycountrycode):
    res_1 = requests.get("http://182.150.59.32:18000/backend/api/collect/?operator=" + mycountrycode + "&random=1")
    print(res_1.text)
    res_2 = json.loads(res_1.text)
    res_3 = res_2["data"]
    if res_3["build_release"] == "9" :
        get_deviceinfo(mycountrycode)
    else:
        res_3["build_cpu_abi"] = "armeabi-v8a"
        res_3["build_cpu_abi2"] = ""

        res_4 = json.dumps(res_3)
        file = open("deviceInfo.txt", "w")
        file.write(res_4)
        file.close()
    pass

# def changedevice(path, name, country, flag):
def changedevice(path, name):
    # file = open(path + "\\" + name, "r")
    file = open("deviceInfo.txt", "r")

    # file2 = open("mobile_network_code.txt")
    # res2 = json.loads(file2.read())
    # print(res2)
    # cou = res2[country]
    # print(cou)
    #
    # for key, value in cou:
    #     a = country
    #     b = key
    #     c = value

    # a = "AU"
    # b = "50503"
    # c = "Vodafone"

    # a = "IN"
    # b = "40472"
    # c = "Cellone"

    # a = "BR"
    # b = "72403"
    # c = "TIMBRASIL"

    # a = "ID"
    # b = "51021"
    # c = "INDOSAT"

    # a = "SG"
    # b = "52504"
    # c = "SGP-M1-3GSM"

    # a = "TW"
    # b = "46606"
    # c = "TUNTEX"

    # a = "HK"
    # b = "45401"
    # c = "CITIC Telecom"

    # a = "MY"
    # b = "50216"
    # c = "DiGi"

    # a = "PH"
    # b = "51503"
    # c = "SMART"

    # a = "TH"
    # b = "52020"
    # c = "ACeS"

    # a = "VN"
    # b = "45202"
    # c = "VINAFONE"


    res = json.loads(file.read())
    file.close()

    gaid = res["google_adid"]
    # if flag == True:

    # res["tele_getnetworkcountryiso"] = a
    # res["tele_getsimcountryiso"] = a
    # res["tele_getnetworkoperator"] = b
    # res["tele_getsimoperator"] = b
    # res["tele_getsimoperatorname"] = c
    # res["tele_getnetworkoperatorname"] = c

    # file = open("deviceInfo.txt", "w")
    # j = json.dumps(res)
    # file.write(j)
    # file.close()
    # os.remove(path + "\\" + name)
    return gaid


def changetask(package, url):
    file = open("taskInfo.txt", "r")
    res = json.loads(file.read())
    file.close()

    res["package_name"] = package
    res["offer_url"] = url

    file = open("taskInfo.txt", "w")
    j = json.dumps(res)
    file.write(j)
    file.close()


def change911(path, country, prot):
    cmd = "c: && cd " + path + " && Autoproxytool.exe -changeproxy/" + \
          country + " -proxyport=" + prot
    p = os.popen(cmd)
    p.close()


def pushfile():
    cmd = "adb push D:\\PythonCode\\test1\\Android_use\\Push_Offer\\taskInfo.txt /sdcard/"
    cmd2 = "adb push D:\\PythonCode\\test1\\Android_use\\Push_Offer\\deviceInfo.txt /sdcard/"
    p1 = os.popen(cmd)
    p1.close()

    p2 = os.popen(cmd2)
    p2.close()


if __name__ == "__main__":
    # country = "IN"

    path = "JP_json_file"
    # flag = True

    # country = "US";package = "us.android.mingzhi.motv";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96550167&affSub=5328109&gaid="
    # country = "IN";package = "com.myntra.android";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96546960&gaid="

    # country = "IN";package = "com.graymatrix.did";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96546959&gaid="
    # country = "IN";package = "com.gopaysense.android.boost";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96546958&gaid="
    # country = "KR";package = "kr.co.plat.carplat";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96550387&gaid="

    # country = "MY";package = "com.setel.mobile";url = "http://bingmob.offerstrack.net/index.php?offer_id=3362304&aff_id=462&gaid="
    # country = "KR";package = "com.socialapps.homeplus";url = "http://bingmob.offerstrack.net/index.php?offer_id=3334017&aff_id=462&gaid="
    # country = "IN";package = "com.rapido.passenger";url = "http://bingmob.offerstrack.net/index.php?offer_id=3334000&aff_id=462&gaid="
    # country = "IN";package = "com.meesho.supply";url = "http://bingmob.offerstrack.net/index.php?offer_id=3333999&aff_id=462&gaid="
    # country = "BR";package = "com.hipercard.app";url = "http://bingmob.offerstrack.net/index.php?offer_id=3333992&aff_id=462&gaid="


    # country = "JP";package = "jp.mbga.a12016007.lite";url = "http://global.ymtracking.com/trace?offer_id=21221143&aff_id=111819&gaid="--0 跳转到jp.jun.yoshida.paddy
    # country = "JP";package = "askiss.game.nouenkonkatsu";url = "http://dopemobi.offerstrack.net/index.php?offer_id=92439&aff_id=1252&gaid="--911的网络跳转失败，affilitest跳转成功
    # country = "JP";package = "askiss.game.bokujoukonkatsu";url = "http://dopemobi.offerstrack.net/index.php?offer_id=92436&aff_id=1252&gaid="--911的网络跳转失败，affilitest跳转成功
    # country = "JP";package = "com.decurret.walletapp";url = "http://dopemobi.offerstrack.net/index.php?offer_id=92405&aff_id=1252&gaid="


    # country = "HK";package = "com.tw.king";url = "http://global.ymtracking.com/trace?offer_id=19094510&aff_id=111819&gaid="
    # country = "TW";package = "tw.sonet.wcp";url = "https://gametraffic.g2afse.com/click?pid=39&offer_id=898&gaid="
    # country = "PH";package = "com.oyo.consumer";url = "https://play.google.com/store/apps/details?id=com.oyo.consumer&gaid="
    # country = "KR";package = "com.netmarble.kofkr";url = "http://dopemobi.offerstrack.net/index.php?offer_id=88643&aff_id=1252&gaid="
    # country = "VN";package = "com.vgm.muh5";url = "http://global.ymtracking.com/trace?offer_id=20381849&aff_id=111819&gaid="
    # country = "MY";package = "com.vuclip.viu";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=9655272&gaid="

    # country = "HK";package = "com.eskyfun.sgsmjz";url = "http://track.mobiproud.com/data/click?cid=-AJIHCs5RL6bgPJHVUzTrg&affid=brfLKnvbROyjRYY3ZernuQ&gaid="
    # country = "IN";package = "com.graymatrix.did";url = "http://clk.holasong.com/click?id=1109593&aff=143&ost=1574336575&gaid="
    # country = "IN";package = "com.goibibo";url = "http://clk.holasong.com/click?id=1136663&aff=143&ost=1574336575&gaid="--Failure [INSTALL_FAILED_VERIFICATION_FAILURE]
    # country = "ph";package = "com.ing.asia.mobil";url = "http://clk.holasong.com/click?id=699618&aff=143&ost=1574336575&gaid="--410 - Page Deleted or Gone
    # country = "JP";package = "com.asobimo.avabel_gp_b3";url = "http://clk.holasong.com/click?id=1122215&aff=143&ost=1574336724&gaid="
    # country = "JP";package = "jp.gungho.bm";url = "http://dopemobi.offerstrack.net/index.php?offer_id=97356&aff_id=1252&gaid="
    # country = "JP";package = "com.complexlove";url = "http://dopemobi.offerstrack.net/index.php?offer_id=97471&aff_id=1252&gaid="
    # country = "US";package = "com.psafe.msuite";url = "http://api.bdisl.com/redirect?s=5328109&at=4&rt=api&o=96540361gaid="--Failure [INSTALL_FAILED_VERIFICATION_FAILURE]

    # country = "JP";package = "com.fundoshiparade.bokukoro3jp";url = "http://dopemobi.offerstrack.net/index.php?offer_id=99234&aff_id=1252&google_aid="
    # country = "JP";package = "com.decurret.walletapp";url = "http://clk.holasong.com/click?id=1196760&aff=143&ost=1574676698&gaid="
    # country = "JP";package = "com.sunborn.girlsfrontline.jp";url = "http://clk.holasong.com/click?id=1196762&aff=143&ost=1574676698&gaid="
    # country = "JP";package = "com.kayac.koshien_pocket";url = "http://clk.holasong.com/click?id=1196752&aff=143&ost=1574676698&gaid="
    # country = "TH";package = "com.hb.hungryhub";url = "http://dopemobi.offerstrack.net/index.php?offer_id=99254&aff_id=1252&google_aid="
    # country = "TW";package = "com.uwvi.tw.app";url = "http://dopemobi.offerstrack.net/index.php?offer_id=99253&aff_id=1252&google_aid="
    # country = "JP";package = "jp.hotpepper.android.beauty.hair";url = "http://dopemobi.offerstrack.net/index.php?offer_id=99579&aff_id=1252&google_aid="
    # country = "JP";package = "com.Level5.YWP";url = "http://dopemobi.offerstrack.net/index.php?offer_id=99228&amp;aff_id=1252&google_aid="


    # country = "IN";package = "com.makemytrip";url = "http://enjoynet.fuse-ad.com/tl?a=26&o=858&gaid="
    # country = "IN";package = "com.avail.easyloans.android";url = "http://enjoynet.fuse-ad.com/tl?a=26&o=855&gaid="
    # country = "JP";package = "com.cydonia.asharmdolls";url = "https://app.adjust.com/p2267ni"

    # country = "TW";package = "com.igs.kovtw";url = "http://clkbb.tbnetwork.im/click?id=7240696&aff=555&ost=1575513315&gaid="

    # country = "JP";package = "com.indiaBulls";url = "http://ai.adtarget.tech/trace?offer_id=21219228&app_id=1101&type=fec5ea690000000c&gaid=" --[INSTALL_FAILED_VERIFICATION_FAILURE]
    # country = "JP";package = "com.fiverr.fiverr";url = "http://ai.adtarget.tech/trace?offer_id=13097656&app_id=1101&type=ff69eeba0000002e&gaid="
    # country = "JP";package = "com.dena.mirrativ";url = "http://ai.adtarget.tech/trace?offer_id=21321700&app_id=1101&type=fefa4e910000001b&gaid=" --[INSTALL_FAILED_VERIFICATION_FAILURE]
    # country = "JP";package = "jp.linecorp.linemusic.android";url = "http://ai.adtarget.tech/trace?offer_id=21222304&app_id=1101&type=fee2228500000007&gaid="

    # country = "BR";package = "com.psafe.msuite";url = "http://clkbb.tbnetwork.im/click?id=6473645&aff=555&ost=1575616589&gaid="
    # country = "US";package = "com.psafe.msuite";url = "http://ai.adtarget.tech/trace?offer_id=15717991&app_id=1101&type=1fdc909500000006&gaid="
    # country = "BR";package = "com.psafe.msuite";url = "http://ai.adtarget.tech/trace?offer_id=14118240&app_id=1101&type=5e537a5b0000001a&gaid="
    # country = "BR";package = "com.psafe.msuite";url = "http://ai.adtarget.tech/trace?offer_id=15476177&app_id=1101&type=ff21675000000037&gaid="
    # country = "BR";package = "com.psafe.msuite";url = "http://ai.adtarget.tech/trace?offer_id=13858317&app_id=1101&type=7e4f7ae100000003&gaid="
    # country = "BR";package = "com.psafe.msuite";url = "http://ai.adtarget.tech/trace?offer_id=21274570&app_id=1101&type=1442c31200000027&gaid="



    # country = "ID";package = "com.julofinance.juloapp";url = "http://ai.adtarget.tech/trace?offer_id=16122317&app_id=1101&type=309347de00000000&gaid="--[INSTALL_FAILED_NO_MATCHING_ABIS: Failed to extract native libraries, res=-113]
    # country = "ID";package = "id.dana";url = "http://ai.adtarget.tech/trace?offer_id=15975626&app_id=1101&type=1a71380200000029&gaid="
    country = "ID";package = "com.gojek.life";url = "http://ai.adtarget.tech/trace?offer_id=14599590&app_id=1101&type=2e57971500000012&gaid="
    # country = "ID";package = "com.mintq.gocash";url = "http://ai.adtarget.tech/trace?offer_id=14924433&app_id=1101&type=ff50a69900000019&gaid="
    # country = "ID";package = "com.pegipegi.android";url = "http://ai.adtarget.tech/trace?offer_id=10271828&app_id=1101&type=ff65a0a10000001f&gaid="
    # country = "ID";package = "com.iqoption";url = "http://ai.adtarget.tech/trace?offer_id=21259023&app_id=1101&type=3121251c00000000&gaid="--[INSTALL_FAILED_NO_MATCHING_ABIS: Failed to extract native libraries, res=-113]
    # country = "ID";package = "com.idnada.loan";url = "http://ai.adtarget.tech/trace?offer_id=19167100&app_id=1101&type=feb87e950000002f&gaid="
    # country = "ID";package = "com.mcdonalds.mobileapp";url = "http://ai.adtarget.tech/trace?offer_id=21317085&app_id=1101&type=07d231cf0000002a&gaid="
    # country = "ID";package = "com.alodokter.android";url = "http://ai.adtarget.tech/trace?offer_id=21308375&app_id=1101&type=35bcf78700000009&gaid="
    # country = "ID";package = "com.pegipegi.android";url = "http://ai.adtarget.tech/trace?offer_id=16027984&app_id=1101&type=ff5aa5520000002e&gaid="
    # country = "ID";package = "com.pegipegi.android";url = "http://ai.adtarget.tech/trace?offer_id=19555608&app_id=1101&type=0652934c00000025&gaid="
    # country = "ID";package = "com.pegipegi.android";url = "http://ai.adtarget.tech/trace?offer_id=20428468&app_id=1101&type=fefaf43500000037&gaid="






    # package = "com.kreditzy.android"
    # url = "http://enjoynet.fuse-ad.com/tl?a=26&o=288&gaid=google_aid"
    get_deviceinfo("510")
    # gaid = changedevice(path, file_name(path), country, flag)
    gaid = changedevice(path, file_name(path))
    track_url = url + gaid
    # track_url = url
    changetask(package, track_url)
    pushfile()
    path_911 = "C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\\911\\911S5 2018-0910\\ProxyTool"
    prot = "5000"
    # change911(path_911, country, prot)


