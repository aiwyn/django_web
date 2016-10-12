# -*- coding: utf-8 -*-
from django.db import models
from .const import CampaignConst, WeixinConst
from campaigns.position.const import adminfilter

class Weixin(models.Model):
    name = models.CharField(max_length=100, verbose_name=WeixinConst.VN_NAME)
    key = models.CharField(max_length=200, verbose_name=WeixinConst.VN_KEY)
    secret = models.CharField(max_length=200, verbose_name=WeixinConst.VN_SECRET)
    token = models.CharField(max_length=200, null=True, blank=True, verbose_name=WeixinConst.VN_Token)
    encodingaeskey = models.CharField(max_length=200, null=True, blank=True, verbose_name=WeixinConst.VN_EncodingAESKey)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=WeixinConst.VN_CREATION_TIME)
    updateTime = models.DateTimeField(auto_now=True, verbose_name=WeixinConst.VN_UPDATE_TIME)

    class Meta:
        verbose_name = WeixinConst.VN_TABLE_NAME
        verbose_name_plural = WeixinConst.VN_TABLE_NAME

    def __unicode__(self):
        return self.name


class adminuser(models.Model):
    name = models.CharField(max_length=100, verbose_name=adminfilter.VN_ADMIN_USER)
    passwd = models.CharField(max_length=100, verbose_name=adminfilter.VN_ADMIN_PASSWD)
    userlvl = models.IntegerField(choices=adminfilter.VN_ADMIN_LVL_CHOICE, verbose_name=adminfilter.VN_ADMIN_LVL, default=adminfilter.LVL3)


    class Meta:
        verbose_name = adminfilter.VN_TABLE_NAME
        verbose_name_plural = adminfilter.VN_TABLE_NAME

    def __unicode__(self):
        return self.name

class positinfo(models.Model):
    name = models.CharField(max_length=100, verbose_name=adminfilter.VN_POST_NAME)
    long = models.FloatField(verbose_name=adminfilter.VN_LONG)
    lat = models.FloatField(verbose_name=adminfilter.VN_LAT)

