# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .const import WorkConst
from campaigns.foundation.const import FoundationConst
from .applet import cheat
from campaigns.foundation.actions import action_export_excel, form_platform_validate
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'creatime']
    list_filter = ['id']



admin.site.register(Data, DataAdmin)
