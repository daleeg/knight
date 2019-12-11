#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests
import logging
from urllib.parse import urljoin
from requests.sessions import Session
import random

LOG = logging.getLogger(__name__)

USER_AGENTS = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Mobile/15E148 MicroMessenger/7.0.8(0x17000820) NetType/WIFI",
]
XHS_BASE_HOST = "www.xiaohongshu.com"


class WxXhsApi(object):
    def __init__(self, host=XHS_BASE_HOST, prefix="wx_mp_api/sns/v1/", scheme="https"):
        self._host = host
        self._prefix = prefix
        self._base_url = "{}://{}/{}".format(scheme, host, prefix)

        self._session = Session()
        ui = random.randint(0, len(USER_AGENTS) - 1)
        headers = {
            "User-Agent": USER_AGENTS[ui],
            "Host": self._host,
            "Connection": "close",
            "Accept-Encoding": "br, gzip, deflate",
            "Content-Type": "application/json",
            "Accept-Language": "zh-cn",
            "Device-Fingerprint":
                "WHJMrwNw1k/Gy/sC6Z1D0XzFNbmyE3cyfJCjTR5D+eJ4GPjHvuEU1skE1O3fkhMVWGWPZ3E6FqIOaBmFkRMqt6xFlRX"
                "tfTfVBdCW1tldyDzmauSxIJm5Txg==1487582755342",
            "Authorization": "ea521d9b-c1fb-4f91-8560-bfa160171e5a"
        }
        sid = "1572606846528931138054"
        self._sid = "session.{}".format(sid)
        self._session.headers.update(headers)
        self._session.keep_alive = False

    def _get(self, route, params=None, retry=1):
        url = urljoin(self._base_url, route)
        if params:
            params.update(sid=self._sid)

        try:
            ret = self._session.get(url, params=params, timeout=(5, 10))
            LOG.info("GET {} {}".format(ret.url, ret.status_code))
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError)as e:
            LOG.error(e)
            return None

        error = ret.text
        if 200 <= ret.status_code < 300:
            ret.encoding = 'utf-8'
            data = ret.json()
            success = data.get("success")
            if success:
                return data["data"]
            else:
                print("result:{}-{}".format(data.get("result"), data.get("msg")))
        if retry:
            return self._get(route, params, retry - 1)
        raise Exception('Error url:{} -{}'.format(url, error))

    # def get_homefeed_categories(self):
    #     route = "homefeed/categories"
    #     result = self._get(route)
    #     return result
    #
    # def get_search_tending(self):
    #     route = "search/trending"
    #     result = self._get(route)
    #     return result

    def search_notes(self, keyword, sort="general", page=1, per_page=20):
        route = "search/notes"
        params = {
            "keyword": keyword,
            "page": page,
            "per_page": per_page,
            "sort": sort
        }
        result = self._get(route, params)
        return result

    def get_note_info_list(self, note_id):
        route = "note/{}/single_feed".format(note_id)
        result = self._get(route)
        return result

    def close(self):
        return self._session.close()


if __name__ == "__main__":
    xhs = WxXhsApi()
    import sys
    import io
    import time
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    notes = xhs.search_notes("book")
    print("total_count:{}".format(notes["total_count"]))
    for note in notes["notes"]:
        _note_id = note["id"]
        title = note["title"]
        print("id:{}".format(_note_id))
        print("title: {}".format(title))
        note_info_list= xhs.get_note_info_list(_note_id)
        for note_info in note_info_list:
            note_list = note_info["note_list"]
            for _note in note_list:
                print("desc:{}".format(_note["desc"]))
                images_list = _note["images_list"]
                for image in images_list:
                    print("{}".format(image["original"]))
        print("{}".format("-"*20))
        time.sleep(2)

    xhs.close()
