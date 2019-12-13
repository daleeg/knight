# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.urls import path
from yurnero.api import endpoints as eps

urlpatterns = [
    path('note_search/', eps.NoteSearchEndpoint.as_view()),
]
