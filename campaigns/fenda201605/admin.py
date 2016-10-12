# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .const import WorkConst
from campaigns.foundation.const import FoundationConst
from .models import WXUser, Author, Work, Share, Vote, VoteCheat, PageView, UniqueVisitor
from .applet import cheat
from campaigns.foundation.actions import action_export_excel, form_platform_validate


class WXUserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'city', 'gender', 'status', 'creationTime']
    list_filter = ['status', 'creationTime']
    search_fields = ['uuid', 'nickname']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def full_clean(self):
        super(AuthorForm, self).full_clean()
        if self.is_valid():
            form_platform_validate(self)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'gender', 'school', 'platform', 'status', 'creationTime']
    list_filter = ['platform', 'status', 'creationTime']
    search_fields = ['uuid', 'name', 'school']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]
    form = AuthorForm


class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag', 'author', 'type', 'sharedCount', 'votedCount', 'status', 'creationTime']
    list_filter = ['type', 'status', 'creationTime']
    list_editable = ['status']
    search_fields = ['id']
    readonly_fields = ['sharedCount', 'votedCount', 'creationTime', 'image_tag']
    actions = [action_export_excel(), ]

    def image_tag(self, obj):
        return format_html(FoundationConst.TAG_LIST_DISPLAY_IMAGE, obj.image.url)
    image_tag.short_description = WorkConst.SD_IMAGE_TAG


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


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'

    def full_clean(self):
        super(VoteForm, self).full_clean()
        if self.is_valid():
            form_platform_validate(self)


class VoteAdmin(admin.ModelAdmin):
    list_display = ['work', 'platform', 'status', 'creationTime', 'ip', 'wxUser']
    list_filter = ['platform', 'status', 'creationTime']
    search_fields = ['work_id']
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
            vcp = cheat.VoteCheatProcess(obj)
            vcp.start()


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['url', 'ip', 'creationTime']
    list_filter = ['url', 'creationTime']
    search_fields = ['url']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]


class UniqueVisitorAdmin(admin.ModelAdmin):
    list_display = ['url', 'wxUser', 'ip', 'creationTime']
    list_filter = ['url', 'creationTime']
    search_fields = ['url']
    readonly_fields = ['creationTime']
    actions = [action_export_excel(), ]


admin.site.register(WXUser, WXUserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Share, ShareAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(VoteCheat, VoteCheatAdmin)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(UniqueVisitor, UniqueVisitorAdmin)
