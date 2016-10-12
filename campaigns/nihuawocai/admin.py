# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Guessodds
from .const import CampaignConst
from campaigns.foundation.actions import action_export_excel


class GuessAdmin(admin.ModelAdmin):
    list_display = ['id', 'odds']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Guessodds, GuessAdmin)