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
    "Mobile/15E148 swan/2.12.5 swan-baiduboxapp/11.16.5.16 baiduboxapp/11.16.5.16 (Baidu; P2 12.3.1)",
]
XHS_BASE_HOST = "www.xiaohongshu.com"


class BdXhsApi(object):
    def __init__(self, host=XHS_BASE_HOST, prefix="fe_api/burdock/baidu/v2/", scheme="https"):
        self._host = host
        self._prefix = prefix
        self._base_url = "{}://{}/{}".format(scheme, host, prefix)

        self._session = Session()
        ui = random.randint(0, len(USER_AGENTS) - 1)
        headers = {
            "User-Agent": USER_AGENTS[ui],
            "Host": self._host,
            "Connection": "close",
            "Content-Type": "application/json",
            "Accept-Language": "zh-cn"
        }
        self._session.headers.update(headers)
        self._session.keep_alive = False

    def _get(self, route, sign_code, retry=1):
        url = urljoin(self._base_url, route)
        headers = {
            "X-Sign": "X{}".format(sign_code)
        }
        try:
            ret = self._session.get(url, headers=headers, timeout=(2, 5))
            LOG.info("GET {} {}".format(ret.url, ret.status_code))
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError)as e:
            LOG.error(e)
            return None

        error = ret.text
        import pdb
        pdb.set_trace()
        if 200 <= ret.status_code < 300:
            data = ret.json()
            code = data.get("code")
            if code == 0:
                return data["data"]
        if retry:
            return self._get(route, sign_code, retry - 1)
        raise Exception('Error url:{} -{}'.format(url, error))

    def get_homefeed_categories(self):
        route = "homefeed/categories"
        sign_code = "144fc3e8f0039f6fdf80d42152805e2d"
        result = self._get(route, sign_code=sign_code)
        return result

    def get_search_tending(self):
        route = "search/trending"
        sign_code = "1d2bce3df0a71e0b906c0ef74a7637ab"
        result = self._get(route, sign_code=sign_code)
        return result

    def close(self):
        return self._session.close()


if __name__ == "__main__":
    xhs = BdXhsApi()
    categories = xhs.get_homefeed_categories()
    for item in categories:
        print("{}:{}".format(item["name"], item["oid"]))

    tending = xhs.get_search_tending()
    for item in tending:
        print("{}:{}".format(item["type"], item["name"]))

    xhs.close()