# -*- coding: utf-8 -*-
from django.db import models
from .config import WorkConfig
from .const import *
from campaigns.foundation.const import FoundationConst
from campaigns.foundation.applet.utils import handle_image_upload



# 作品表
class YQWork(models.Model):
    ImageFront = models.CharField(max_length=100000, default=' ', verbose_name=FoundationConst.VN_FRONT)
    ImageBack = models.CharField(max_length=100000, default=' ', verbose_name=FoundationConst.VN_BACK)
    # ImageSBack = models.ImageField(upload_to=handle_image_upload(WorkConfig.REL_PATH_IMAGE), verbose_name=FoundationConst.VN_BACK)
    # ImageSFront = models.ImageField(upload_to=handle_image_upload(WorkConfig.REL_PATH_IMAGE), verbose_name=FoundationConst.VN_SFRONT)
    ImageSBack = models.ImageField(upload_to='', verbose_name=FoundationConst.VN_BACK)
    ImageSFront = models.ImageField(upload_to='', verbose_name=FoundationConst.VN_SFRONT)
    fixstatus = models.IntegerField(choices=FoundationConst.FIX_STATUS_CHOICES, verbose_name=FoundationConst.VN_FIX)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)
    votedCount = models.IntegerField(default=0, verbose_name=FoundationConst.VN_VOTED_COUNT)
    openid = models.CharField(max_length=200)
    status = models.IntegerField(choices=FoundationConst.STATUS_CHOICES, default=0,verbose_name=FoundationConst.VN_STATUS)

    class Meta:
        verbose_name = WorkConst.VN_TABLE_NAME
        verbose_name_plural = WorkConst.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)


# 刷作品
class CheatWork(models.Model):
    count = models.IntegerField(verbose_name=FoundationConst.VN_WORKCOUNT)
    creationtime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)


    class Meta:
        verbose_name = WorkCount.VN_TABLE_NAME
        verbose_name_plural = WorkCount.VN_TABLE_NAME


    def __uncode__(self):
        return WorkCount.VN_TABLE_NAME


# 打印碼表
class PrintWork(models.Model):
    size = models.IntegerField(choices=FoundationConst.SIZE_CHOICES, verbose_name=FoundationConst.VN_SIZE, default=FoundationConst.SIZEL)
    colors = models.IntegerField(choices=FoundationConst.COLOR_CHOICES, verbose_name=FoundationConst.VN_COLORS, default=FoundationConst.black)
    openid = models.CharField(max_length=200)
    printcode = models.CharField(max_length=200, verbose_name=FoundationConst.VN_PRINTID, null=True, blank=True)
    isprint = models.IntegerField(choices=FoundationConst.PRINT_CHOICES, verbose_name=FoundationConst.VN_PRINT, default=FoundationConst.UNPRINT)
    workid = models.CharField(max_length=100, verbose_name=FoundationConst.VN_ID)


# 微信用户表
class WXUser(models.Model):
    openid = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100, null=True, blank=True, verbose_name=FoundationConst.VN_NICKNAME)
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name=FoundationConst.VN_CITY)
    gender = models.IntegerField(choices=FoundationConst.GENDER_CHOICES, verbose_name=FoundationConst.VN_GENDER)
    fixstatus = models.IntegerField(choices=FoundationConst.FIX_STATUS_CHOICES, verbose_name=FoundationConst.VN_FIX)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)
    comment = models.CharField(max_length=100, null=True, blank=True, verbose_name=FoundationConst.VN_COMMENT)
    class Meta:
        verbose_name = WXUserConst.VN_TABLE_NAME
        verbose_name_plural = WXUserConst.VN_TABLE_NAME

    def __unicode__(self):
        return self.openid


# UV表
class UniqueVisitor(models.Model):
    url = models.URLField(verbose_name=FoundationConst.VN_URL)
    wxUser = models.ForeignKey(WXUser, null=True, blank=True, verbose_name=WXUserConst.VN_TABLE_NAME)
    ip = models.GenericIPAddressField(verbose_name=FoundationConst.VN_IP)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = UniqueVisitorConst.VN_TABLE_NAME
        verbose_name_plural = UniqueVisitorConst.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)


# PV表
class PageView(models.Model):
    url = models.URLField(verbose_name=FoundationConst.VN_URL)
    ip = models.GenericIPAddressField(verbose_name=FoundationConst.VN_IP)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = PageViewConst.VN_TABLE_NAME
        verbose_name_plural = PageViewConst.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)


# 分享表单
class Share(models.Model):
    url = models.URLField(verbose_name=FoundationConst.VN_URL)
    work = models.ForeignKey(YQWork, null=True, blank=True, verbose_name=WorkConst.VN_TABLE_NAME)
    platform = models.IntegerField(choices=FoundationConst.PLATFORM_CHOICES, verbose_name=FoundationConst.VN_PLATFORM)
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=FoundationConst.VN_IP)
    wxUser = models.ForeignKey(WXUser, null=True, blank=True, verbose_name=WXUserConst.VN_TABLE_NAME)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = ShareConst.VN_TABLE_NAME
        verbose_name_plural = ShareConst.VN_TABLE_NAME

    def __unicode__(self):
        return ShareConst.VN_TABLE_NAME

    def save(self, *args, **kwargs):
        if self.work is not None:
            self.work.sharedCount = Share.objects.filter(work=self.work).count() + 1
            self.work.save()
        super(Share, self).save(*args, **kwargs)


class Vote(models.Model):
    work = models.ForeignKey(YQWork, verbose_name=WorkConst.VN_TABLE_NAME)
    platform = models.IntegerField(choices=FoundationConst.PLATFORM_CHOICES, verbose_name=FoundationConst.VN_PLATFORM)
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=FoundationConst.VN_IP)
    wxUser = models.ForeignKey(WXUser, null=True, blank=True, verbose_name=WXUserConst.VN_TABLE_NAME)
    status = models.IntegerField(choices=FoundationConst.FIX_STATUS_CHOICES, verbose_name=FoundationConst.VN_FIX)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = VoteConst.VN_TABLE_NAME
        verbose_name_plural = VoteConst.VN_TABLE_NAME

    def __unicode__(self):
        return VoteConst.VN_TABLE_NAME

    def save(self, *args, **kwargs):
        self.work.votedCount = Vote.objects.filter(work=self.work).filter(status=FoundationConst.STATUS_ONLINE).count() + 1
        self.work.save()
        super(Vote, self).save(*args, **kwargs)


class VoteCheat(models.Model):
    comment = models.CharField(max_length=100, verbose_name=FoundationConst.VN_COMMENT)
    type = models.IntegerField(choices=VoteCheatConst.TYPE_CHOICES, verbose_name=FoundationConst.VN_TYPE)
    minute = models.IntegerField(verbose_name=FoundationConst.VN_MINUTE)
    totalCount = models.IntegerField(verbose_name=FoundationConst.VN_TOTAL_COUNT)
    nowCount = models.IntegerField(null=True, blank=True, verbose_name=FoundationConst.VN_NOW_COUNT, default=0)
    work = models.ForeignKey(YQWork, null=True, blank=True, verbose_name=WorkConst.VN_TABLE_NAME)
    ip = models.GenericIPAddressField(verbose_name=FoundationConst.VN_IP, default=FoundationConst.DEFAULT_IP)
    hasFinished = models.BooleanField(verbose_name=FoundationConst.VN_HAS_FINISHED, default=False)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)
    updateTime = models.DateTimeField(auto_now=True, verbose_name=FoundationConst.VN_UPDATE_TIME)

    class Meta:
        verbose_name = VoteCheatConst.VN_TABLE_NAME
        verbose_name_plural = VoteCheatConst.VN_TABLE_NAME

    def __unicode__(self):
        return self.comment
