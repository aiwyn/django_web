# -*- coding: utf-8 -*-
from django.contrib import admin
from .const import CampaignConst
from campaigns.foundation.actions import action_export_excel
from models import imbatman, activetime, activeinfo, prizes
from campaigns.testproject.applet.activeobj import ActiveobjAdmin, PrizesobjAdmin


class ImbatmanAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_date', 'headline', 'content']
    actions = [action_export_excel(), ]


class ActiveTimeAdmin(admin.ModelAdmin):
    list_display = ['activename', 'chance', 'starttime', 'stoptime', 'ucount', 'dcount']
    list_filter = ['activename']
    search_fields = ['id']
    readonly_fields = ['id', 'activedays']
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


class Prizesfetch(admin.ModelAdmin):
    list_display = ['id', 'prizeslvl', 'isdole', 'userid', 'activeid', 'prizesname']
    list_filter = ['activeid']
    search_fields = ['prizesname']
    readonly_fields = ['prizeslvl', 'isdole', 'userid', 'activeid', 'prizesname', 'activetime']
    actions = [action_export_excel(), ]


admin.site.register(imbatman, ImbatmanAdmin)
admin.site.register(activetime, ActiveTimeAdmin)
admin.site.register(activeinfo, ActiveInfoAdmin)
admin.site.register(prizes, Prizesfetch)