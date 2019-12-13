# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

# return code
SUCCESS = 0

UNKNOWN_ERROR = 0x101
BAD_REQUEST = 0x102
NO_PERMISSION = 0x103
AUTHENTICATION_FAILED = 0x104
NOT_AUTHENTICATED = 0x105
NOT_SUPPORT = 0x106
DATABASE_ERROR = 0x107
DATA_CONFLICT = 0x108
DELETE_FORBIDDEN = 0x109
LOGIN_FAILED = 0x10A
LICENSE_EXPIRING =  0x10B
LICENSE_LIMIT =  0x10C
NOT_FOUND =  0x10D
UPDATE_FORBIDDEN =  0x10E

# return message
RETURN_MSG = {
    SUCCESS: _('正常。'),
    UNKNOWN_ERROR: _('未知错误。'),
    BAD_REQUEST: _('错误请求格式。'),
    NO_PERMISSION: _('无访问权限。'),
    AUTHENTICATION_FAILED: _('用户名或密码错误。'),
    NOT_AUTHENTICATED: _('请登录。'),
    NOT_SUPPORT: _('不支持。'),
    LICENSE_EXPIRING: _('授权已过期或未授权，请联系管理员。'),
    LICENSE_LIMIT: _('超过授权账户最大允许的用户数，请联系管理员。'),
    NOT_FOUND: _("未查询到"),
    DATABASE_ERROR: _('数据库错误'),
    DATA_CONFLICT: _('数据冲突'),
    DELETE_FORBIDDEN: _('禁止删除'),
    LOGIN_FAILED: _('登录失败'),
    UPDATE_FORBIDDEN: _("禁止修改"),
}
