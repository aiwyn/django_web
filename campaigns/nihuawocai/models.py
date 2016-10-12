# -*- coding: utf-8 -*-
from django.db import models
from .const import Guess


class Guessodds(models.Model):
    odds = models.CharField(verbose_name="画图物品", max_length=100, )

    class Meta:
        verbose_name = Guess.VN_TABLES_NAME
        verbose_name_plural = Guess.VN_TABLES_NAME

    def __unicode__(self):
        return self.odds
