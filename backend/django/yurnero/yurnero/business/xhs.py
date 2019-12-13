# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from yurnero.utils.wxxhsapi import WxXhsApi
import time


def search_note_by_wx(search_key, page=1, per_page=20, sort="general"):
    xhs = WxXhsApi()
    result = {}
    notes = xhs.search_notes(search_key, page, per_page, sort)
    result["count"] = notes["total_count"]
    result["results"] = []

    for note in notes["notes"]:
        _note_id = note["id"]
        title = note["title"]

        note_info_list = xhs.get_note_info_list(_note_id)
        time.sleep(0.1)
        items = []
        for note_info in note_info_list:
            note_list = note_info["note_list"]
            for _note in note_list:
                desc = _note["desc"]
                images_list = _note["images_list"]
                item = {
                    "desc": desc,
                    "images_list": [image["original"] for image in images_list]
                }
                items.append(item)
        note_item = {
            "id": _note_id,
            "title": title,
            "note_list": items
        }

        result["results"].append(note_item)
    xhs.close()
    return result