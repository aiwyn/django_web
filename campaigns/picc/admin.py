# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .const import WorkConst
from campaigns.foundation.const import FoundationConst
from .models import WXUser, Work, Vote, VoteCheat, PageView, UniqueVisitor
from .applet import cheat
from campaigns.foundation.actions import action_export_excel, form_platform_validate

class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "dream", 'votedCount']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        obj.save()

class VoteCheatAdmin(admin.ModelAdmin):
    list_display = ['comment', 'type', 'minute', 'totalCount', 'nowCount', 'hasFinished', 'creationTime', 'updateTime']
    list_filter = ['type']
    search_fields = ['comment']
    readonly_fields = ['creationTime', 'updateTime', 'hasFinished']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.nowCount == 0:
            vcp = cheat.VoteCheatProcess(obj)
            vcp.start()

class VoteAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_filter = ['wxUser']

class WXUserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'city', 'gender', 'status', 'creationTime']
    list_filter = ['status', 'creationTime']
    search_fields = ['uuid', 'nickname']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]


class PvAdmin(admin.ModelAdmin):
    list_display = ['id']


class UvAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(PageView, PvAdmin)
admin.site.register(UniqueVisitor, UvAdmin)
admin.site.register(WXUser, WXUserAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(VoteCheat, VoteCheatAdmin)