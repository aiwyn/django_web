# -*- coding: utf-8 -*-
from django.db import models
from .const import CampaignConst, Momangers, UserConst, PageViewConst, UniqueVisitorConst, UsrPoint, InfoConst, TimeConst, PrizesConst
from campaigns.foundation.const import FoundationConst
from DjangoUeditor.models import UEditorField


# 奖品表
class prizes(models.Model):
    prizeslvl = models.IntegerField(verbose_name=FoundationConst.VN_PRIZES, choices=FoundationConst.PRIZES_CHOICES)
    isdole = models.IntegerField(choices=FoundationConst.IS_DOLE_CHOICES, verbose_name=FoundationConst.VN_ISDOLE, default=FoundationConst.UNDOLE)
    userid = models.CharField(max_length=200, null=True, blank=True, verbose_name=FoundationConst.VN_USER)
    activeid = models.IntegerField(verbose_name=FoundationConst.VN_ACTIVEID)
    prizesname = models.CharField(max_length=200, verbose_name=FoundationConst.VN_PRINAME)
    activetime = models.IntegerField(verbose_name=FoundationConst.VN_REDATE)
    isdone = models.IntegerField(verbose_name=FoundationConst.VN_DONE, choices=FoundationConst.IS_DONE_CHOICES, default=FoundationConst.UNDONE)

    class Meta:
        verbose_name = PrizesConst.VN_TABLE_NAME
        verbose_name_plural = PrizesConst.VN_TABLE_NAME


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



class Mangers(models.Model):
    name = models.CharField(max_length=200, verbose_name=Momangers.RN_USR_NAME)
    passwd = models.CharField(max_length=200, verbose_name=Momangers.RN_USR_PASSWD)
    usrnum = models.CharField(max_length=100, verbose_name=Momangers.RN_USR_NUM)
    display = models.ImageField(upload_to='', verbose_name=Momangers.RN_USR_DISPLAY)
    openid = models.CharField(verbose_name=Momangers, null=True, blank=True, max_length=200)
    usraddr = models.CharField(max_length=200, null=True, blank=True, verbose_name=Momangers.RN_USR_PASSWD)
    gender = models.IntegerField(choices=FoundationConst.GENDER_CHOICES, verbose_name=Momangers.RN_USR_SEX)
    point = models.IntegerField(null=True, blank=True, verbose_name=Momangers.RN_USR_POINT)

    class Meta:
        verbose_name = UserConst.VN_TABLE_NAME
        verbose_name_plural = UserConst.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)


class usrpoint(models.Model):
    info = models.ForeignKey(Mangers, verbose_name=Momangers.RN_USR_NAME)
    datetime = models.DateField(verbose_name=Momangers.RN_USR_DATE, null=True, blank=True)
    continuity = models.IntegerField(null=True, blank=True, verbose_name=Momangers.RN_USR_CONTINUE)
    point = models.IntegerField(null=True, blank=True, verbose_name=Momangers.RN_USR_POINT)

    class Meta:
        verbose_name = UsrPoint.VN_TABLE_NAME
        verbose_name_plural = UsrPoint.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)


class PageView(models.Model):
    url = models.URLField(verbose_name=FoundationConst.VN_URL)
    ip = models.GenericIPAddressField(verbose_name=FoundationConst.VN_IP)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = PageViewConst.VN_TABLE_NAME
        verbose_name_plural = PageViewConst.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)


class UniqueVisitor(models.Model):
    url = models.URLField(verbose_name=FoundationConst.VN_URL)
    wxUser = models.ForeignKey(Mangers, null=True, blank=True, verbose_name=UserConst.VN_TABLE_NAME)
    ip = models.GenericIPAddressField(verbose_name=FoundationConst.VN_IP)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=FoundationConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = UniqueVisitorConst.VN_TABLE_NAME
        verbose_name_plural = UniqueVisitorConst.VN_TABLE_NAME

    def __unicode__(self):
        return str(self.id)

class imbatman(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    # content = models.CharField(max_length=10000000)
    content = UEditorField(u'something ', width=600, height=300, toolbars="full", imagePath="", filePath="",upload_settings={"imageMaxSize": 1204000},settings={}, command=None, blank=True)
