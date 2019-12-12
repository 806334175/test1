
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SOL23 Build/14.3.C.0.300) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}


def test():
    url = "https://click.dl-now.app/click?pid=c0750b43-6e4b-41cd-8e57-2a2635fc1f29&click_id=D90FCC13-B07F-4D68-B722-AA3545C85AB6-26181216&gaid=54991b46-a48c-4dbd-89f5-2e76967cd129&scr_id=102&subid_5=102&category=Role+Playing&android_category=Role+Playing&app=,com.netmarble.teraorigin&subid_1=1136&subid_2=5da062bf6d8758616559a6f7&subid_3=5028&subid_4=5da059a26d875816f84acc5c&CQT=1"

    session = requests.session()
    response = session.post(url, headers=HEADERS)
    pass

if __name__ == "__main__":
    pass