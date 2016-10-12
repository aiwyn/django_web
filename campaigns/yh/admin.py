# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .const import WorkConst
from campaigns.foundation.const import FoundationConst
from .models import WXUser, Author, Work, Share, Vote, VoteCheat, PageView, UniqueVisitor
from .applet import cheat
from campaigns.foundation.actions import action_export_excel, form_platform_validate


class wxUserAdmin(admin.ModelAdmin):
    list_display = ['openid', 'nickname', 'creationTime']
    list_filter = ['id']
    search_fields = ['id']
    readonly_fields = []
    actions = [action_export_excel(), ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone', 'creationTime', 'comment']
    search_fields = ['id']
    actions = [action_export_excel(), ]


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'string', 'image_tag', 'author', 'type', 'votedCount', 'status']
    search_fields = ['id']
    list_filter = ['creationTime']
    actions = [action_export_excel()]


    def image_tag(self, obj):
        return format_html(FoundationConst.TAG_LIST_DISPLAY_IMAGE, obj.imageurl)
    image_tag.short_description = WorkConst.SD_IMAGE_TAG


admin.site.register(WXUser, wxUserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Work, WorkAdmin)