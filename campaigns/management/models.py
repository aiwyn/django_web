# -*- coding: utf-8 -*-
from django.db import models
from .const import CampaignConst, Momangers, UserConst, PageViewConst, UniqueVisitorConst, UsrPoint
from campaigns.foundation.const import FoundationConst
from DjangoUeditor.models import UEditorField

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
