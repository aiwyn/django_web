# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Campaign, Weixin
from .const import CampaignConst
from campaigns.foundation.actions import action_export_excel


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weixin','status', 'hasPaused', 'startTime', 'endTime', 'creationTime']
    list_filter = ['status', 'startTime', 'endTime', 'creationTime']
    search_fields = ['name']
    fieldsets = [
        (CampaignConst.FIELDSETS_BASIC, {'fields': ['name', 'status', 'hasPaused', 'startTime', 'endTime']}),
        (CampaignConst.FIELDSETS_KEY, {'fields': ['appName', 'weixin']}),
        (CampaignConst.FIELDSETS_ADDITION, {'fields': ['intro']})
    ]
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]


class WeixinAdmin(admin.ModelAdmin):
    list_display = ['name', 'key', 'creationTime', 'updateTime']
    list_filter = ['creationTime', 'updateTime']
    search_fields = ['name']
    readonly_fields = ['creationTime', 'updateTime']
    actions = [action_export_excel(), ]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Weixin, WeixinAdmin)
