# -*- coding: utf-8 -*-
from django.contrib import admin
from .const import CampaignConst
from campaigns.foundation.actions import action_export_excel
from models import imbatman


class ImbatmanAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_date', 'headline', 'content']
    actions = [action_export_excel(), ]



admin.site.register(imbatman, ImbatmanAdmin)