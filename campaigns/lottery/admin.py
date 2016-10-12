# -*- coding: utf-8 -*-
import multiprocessing
from django.contrib import admin
from django import forms
from django.utils.html import format_html
from models import activetime, activeinfo, Lottery_prizes, lottery_info, test
from campaigns.foundation.actions import action_export_excel, form_platform_validate
from applet.activeobj import ActiveobjAdmin, PrizesobjAdmin, testdelete


class ActiveTimeAdmin(admin.ModelAdmin):
    list_display = ['activename', 'chance', 'starttime', 'stoptime', 'ucount', 'dcount']
    list_filter = ['activename']
    search_fields = ['id']
    readonly_fields = ['id','activedays']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        vcp = ActiveobjAdmin(obj)


class ActiveInfoAdmin(admin.ModelAdmin):
    list_display = ['activeId', 'prizeslvl', 'prizesname', 'quantity', 'releasedate']
    list_filter = ['activeId']
    search_fields = ['activeId']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        vcp = PrizesobjAdmin(obj)
    def delete_model(self, request, obj):
        vip = testdelete(obj)


class Prizesfetch(admin.ModelAdmin):
    list_display = ['id', 'prizeslvl', 'isdole', 'userid', 'activeid', 'prizesname']
    list_filter = ['activeid', 'isdole']
    search_fields = ['prizesname']
    readonly_fields = ['prizeslvl', 'isdole', 'userid', 'activeid', 'prizesname', 'activetime']
    actions = [action_export_excel(), ]

class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_date', 'headline', 'content']
    actions = [action_export_excel(), ]
    class Media:
        js = (
            '/media/tiny_mce/tiny_mce.js',
            '/media/testareas.js',
        )


class UserInfo(admin.ModelAdmin):
    list_display = ['usrname', 'usernum', 'usraddr', 'lottinfo', 'prizesname', 'userid', 'prid']
    list_filter = ['lottinfo']
    search_fields = ['prizesname']
    readonly_fields = ['usrname', 'usernum', 'usraddr', 'lottinfo', 'prizesname', 'userid', 'prid']
    actions = [action_export_excel(), ]
    class Media:
        js = (
            '/media/tiny_mce/tiny_mce.js',
            '/media/textareas.js',
        )


admin.site.register(activetime, ActiveTimeAdmin)
admin.site.register(activeinfo, ActiveInfoAdmin)
admin.site.register(Lottery_prizes, Prizesfetch)
admin.site.register(lottery_info, UserInfo)
admin.site.register(test, TestAdmin)