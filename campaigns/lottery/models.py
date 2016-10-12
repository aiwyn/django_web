# -*- coding: utf-8 -*-
from django.db import models
from .config import WorkConfig
from .const import *
from campaigns.foundation.const import FoundationConst
from campaigns.foundation.applet.utils import handle_image_upload
from tinymce.models import HTMLField
from DjangoUeditor.models import UEditorField

# 后台活动信息
class activeinfo(models.Model):
    activeId = models.IntegerField(verbose_name=FoundationConst.VN_ACTIVEID)
    prizeslvl = models.IntegerField(verbose_name=FoundationConst.VN_PRIZES, choices=FoundationConst.PRIZES_CHOICES)
    prizesname = models.CharField(max_length=300, verbose_name=FoundationConst.VN_PRINAME)
    quantity = models.IntegerField(verbose_name=FoundationConst.VN_QUANTITY)
    releasedate = models.DateField(verbose_name=FoundationConst.VN_REDATE)

    class Meta:
        verbose_name = InfoConst.VN_TABLE_NAME
        verbose_name_plural = InfoConst.VN_TABLE_NAME



# 后台活动时间表
class activetime(models.Model):
    activename = models.CharField(max_length=299, verbose_name=FoundationConst.VN_ACTIVENAME)
    chance = models.FloatField(max_length=10, verbose_name=FoundationConst.VN_CHANCE)
    starttime = models.DateField(verbose_name=FoundationConst.VN_STARTIME)
    stoptime = models.DateField(verbose_name=FoundationConst.VN_STOPTIME)
    activedays = models.IntegerField(verbose_name=FoundationConst.VN_REDATE)
    ucount = models.IntegerField(null=True, blank=True, verbose_name=FoundationConst.VN_UCOUNT)
    dcount = models.IntegerField(null=True, blank=True, verbose_name=FoundationConst.VN_DCOUNT)

    class Meta:
        verbose_name = TimeConst.VN_TABLE_NAME
        verbose_name_plural = TimeConst.VN_TABLE_NAME




# 奖品表
class Lottery_prizes(models.Model):
    prizeslvl = models.IntegerField(verbose_name=FoundationConst.VN_PRIZES, choices=FoundationConst.PRIZES_CHOICES)
    isdole = models.IntegerField(choices=FoundationConst.IS_DOLE_CHOICES, verbose_name=FoundationConst.VN_ISDOLE, default=FoundationConst.UNDOLE)
    userid = models.CharField(max_length=200, null=True, blank=True, verbose_name=FoundationConst.VN_USER)
    activeid = models.IntegerField(verbose_name=FoundationConst.VN_ACTIVEID)
    prizesname = models.CharField(max_length=200, verbose_name=FoundationConst.VN_PRINAME)
    activetime = models.IntegerField(verbose_name=FoundationConst.VN_REDATE)

    class Meta:
        verbose_name = PrizesConst.VN_TABLE_NAME
        verbose_name_plural = PrizesConst.VN_TABLE_NAME



# 用户信息表
class lottery_info(models.Model):
    usrname = models.CharField(max_length=200, verbose_name=FoundationConst.VN_USER)
    usernum = models.CharField(verbose_name=FoundationConst.VN_PHONENU, max_length=50, default=' ')
    usraddr = models.CharField(max_length=300, verbose_name=FoundationConst.VN_ADDRESS, null=True, blank=True)
    lottinfo = models.IntegerField(null=True, blank=True, choices=FoundationConst.PRIZES_CHOICES, verbose_name=FoundationConst.VN_PRIZES)
    prizesname = models.CharField(max_length=300, null=True, blank=True, verbose_name=FoundationConst.VN_PRINAME)
    userid = models.CharField(max_length=200, verbose_name=FoundationConst.VN_ID)
    prid = models.IntegerField(null=True, blank=True, verbose_name=FoundationConst.VN_PRINUM)

    class Meta:
        verbose_name = UsrConst.VN_TABLE_NAME
        verbose_name_plural = UsrConst.VN_TABLE_NAME


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


# 测试富文本编辑器
class test(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.CharField(max_length=10000000)
    # content = UEditorField(u'内容 ', width=600, height=300, toolbars="full", imagePath="", filePath="",upload_settings={"imageMaxSize": 1204000},settings={}, command=None, blank=True)


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




