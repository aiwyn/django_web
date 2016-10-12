# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .const import WorkConst
from campaigns.foundation.const import FoundationConst
from .models import WXUser, YQWork, PrintWork, Share, Vote, VoteCheat, PageView, UniqueVisitor, CheatWork
from campaigns.yiquan.applet.cheat import VoteCheatProcess
from campaigns.foundation.actions import action_export_excel, form_platform_validate
from campaigns.yiquan.applet.activeobj import addwork


class WXUserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'city', 'gender', 'fixstatus', 'creationTime']
    list_filter = ['fixstatus', 'creationTime']
    search_fields = ['uuid', 'nickname']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]


class PrintWorkForm(forms.ModelForm):
    class Meta:
        model = YQWork
        fields = '__all__'

    def full_clean(self):
        super(PrintWorkForm, self).full_clean()
        if self.is_valid():
            form_platform_validate(self)


class PrintWorkAdmin(admin.ModelAdmin):
    list_display = ['workid', 'size', 'colors', 'printcode']
    list_filter = ['printcode', 'size', 'isprint']
    search_fields = ['printcode']
    readonly_fields = ['workid', 'size', 'colors']
    actions = [action_export_excel(), ]
    form = PrintWorkForm



class YQWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'front_image_tag', 'back_image_tag', 'fixstatus', 'creationTime', 'status', 'fetch_work_image_tag']
    list_filter = ['id', 'status', 'creationTime']
    list_editable = ['status']
    search_fields = ['id']
    readonly_fields = ['ImageFront', 'ImageBack', 'ImageSFront', 'ImageSBack']
    actions = [action_export_excel(), ]

    def front_image_tag(self, obj):
        return format_html(FoundationConst.TAG_LIST_DISPLAY_IMAGE, obj.ImageSFront.url)
    front_image_tag.short_description = WorkConst.SD_IMAGE_TAG

    def back_image_tag(self, obj):
        return format_html(FoundationConst.TAG_LIST_DISPLAY_IMAGE, obj.ImageSBack.url)
    back_image_tag.short_description = WorkConst.SD_IMAGE_TAG

    def fetch_work_image_tag(self, obj):
        return format_html(WorkConst.TAG_FETCH_WORK_IMAGE, obj.id)
    fetch_work_image_tag.short_description = WorkConst.SD_FETCH_WORK_IMAGE_TAG


class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = '__all__'

    def full_clean(self):
        super(ShareForm, self).full_clean()
        if self.is_valid():
            form_platform_validate(self)


class ShareAdmin(admin.ModelAdmin):
    list_display = ['url', 'platform', 'creationTime', 'wxUser']
    list_filter = ['platform', 'creationTime', 'wxUser']
    search_fields = ['url']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]
    form = ShareForm


class CheatWorkAdmin(admin.ModelAdmin):
    list_display = ['count']
    list_filter = ['creationtime']
    search_fields = ['id']
    readonly_fields = ['creationtime']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        vcp = addwork(obj)


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'

    def full_clean(self):
        super(VoteForm, self).full_clean()
        if self.is_valid():
            form_platform_validate(self)


class VoteAdmin(admin.ModelAdmin):
    list_display = ['work', 'platform', 'status', 'creationTime']
    list_filter = ['platform', 'status', 'creationTime']
    search_fields = ['work']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]
    form = VoteForm


class VoteCheatAdmin(admin.ModelAdmin):
    list_display = ['comment', 'type', 'minute', 'totalCount', 'nowCount', 'hasFinished', 'creationTime', 'updateTime']
    list_filter = ['type']
    search_fields = ['comment']
    readonly_fields = ['creationTime', 'updateTime', 'hasFinished']
    actions = [action_export_excel(), ]

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.nowCount == 0:
            vcp = VoteCheatProcess(obj)
            vcp.start()


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['url', 'ip', 'creationTime']
    list_filter = ['url', 'creationTime']
    search_fields = ['url']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]





admin.site.register(WXUser, WXUserAdmin)
admin.site.register(PrintWork, PrintWorkAdmin)
admin.site.register(YQWork, YQWorkAdmin)
admin.site.register(Share, ShareAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(VoteCheat, VoteCheatAdmin)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(CheatWork, CheatWorkAdmin)
