# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u540d\u79f0')),
                ('intro', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('appName', models.CharField(max_length=200, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('status', models.IntegerField(verbose_name='\u72b6\u6001', choices=[(0, b'\xe7\xad\x89\xe5\xbe\x85\xe4\xb8\x8a\xe7\xba\xbf'), (10, b'\xe4\xb8\x8a\xe7\xba\xbf\xe4\xb8\xad'), (20, b'\xe5\xb7\xb2\xe7\xbb\x8f\xe7\xbb\x93\xe6\x9d\x9f')])),
                ('hasPaused', models.BooleanField(verbose_name='\u662f\u5426\u6682\u505c')),
                ('startTime', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endTime', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6d3b\u52a8\u4fe1\u606f',
                'verbose_name_plural': '\u6d3b\u52a8\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Weixin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('key', models.CharField(max_length=200, verbose_name='Key')),
                ('secret', models.CharField(max_length=200, verbose_name='Secret')),
                ('token', models.CharField(max_length=200, null=True, verbose_name='Token', blank=True)),
                ('encodingaeskey', models.CharField(max_length=200, null=True, verbose_name='EncodingAESKey', blank=True)),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u4fee\u6539')),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u516c\u4f17\u53f7',
                'verbose_name_plural': '\u5fae\u4fe1\u516c\u4f17\u53f7',
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='weixin',
            field=models.ForeignKey(verbose_name='\u5fae\u4fe1\u516c\u4f17\u53f7', to='foundation.Weixin'),
        ),
    ]
