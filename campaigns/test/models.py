# -*- coding: utf-8 -*-
from django.db import models
from .const import CampaignConst, WeixinConst


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


class Campaign(models.Model):
    name = models.CharField(max_length=200, verbose_name=CampaignConst.VN_NAME)
    intro = models.TextField(null=True, blank=True, verbose_name=CampaignConst.VN_INTRO)
    appName = models.CharField(max_length=200, verbose_name=CampaignConst.VN_APP_NAME)
    status = models.IntegerField(choices=CampaignConst.STATUS_CHOICES, verbose_name=CampaignConst.VN_STATUS)
    hasPaused = models.BooleanField(verbose_name=CampaignConst.VN_HAS_PAUSED)
    startTime = models.DateTimeField(verbose_name=CampaignConst.VN_START_TIME)
    endTime = models.DateTimeField(verbose_name=CampaignConst.VN_END_TIME)
    weixin = models.ForeignKey(Weixin, verbose_name=WeixinConst.VN_TABLE_NAME)
    creationTime = models.DateTimeField(auto_now_add=True, verbose_name=CampaignConst.VN_CREATION_TIME)

    class Meta:
        verbose_name = CampaignConst.VN_TABLE_NAME
        verbose_name_plural = CampaignConst.VN_TABLE_NAME

    def __unicode__(self):
        return self.name

