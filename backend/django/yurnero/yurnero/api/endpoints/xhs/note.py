# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from yurnero.core.endpoint import NoAuthBaseEndpoint
from yurnero.core.response import APIResponse
from yurnero.core.code import BAD_REQUEST
import yurnero.core.schema as ms
from django.utils.encoding import force_text as _t
from yurnero.business.xhs import search_note_by_wx


class NoteSearchEndpoint(NoAuthBaseEndpoint):
    extra_manual_schema = dict(
        get=[
            ms.ManualField(
                name="page",
                schema=ms.STRING(description=_t("A page number within the paginated result set.")),
            ),
            ms.ManualField(
                name="page_size",
                schema=ms.STRING(description=_t("Number of results to return per page")),
            ),
            ms.ManualField(
                name="search",
                schema=ms.STRING(description=_t("检索字符串")),
            ),
        ])


    def get(self, request):
        """
          检索note
        """
        query_params =  request.query_params

        page = query_params.get("page", 1)
        page_size = query_params.get("page_size", 20)
        search_key = query_params.get("search")

        if search_key is None:
            return APIResponse(code=BAD_REQUEST)

        result = search_note_by_wx(search_key, page, page_size)

        return APIResponse(data=result)