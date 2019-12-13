# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
