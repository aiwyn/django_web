# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='\u94fe\u63a5')),
                ('ip', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': 'PV',
                'verbose_name_plural': 'PV',
            },
        ),
        migrations.CreateModel(
            name='PrintWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField(default=2, verbose_name='\u5c3a\u7801', choices=[(0, b'S\xe5\xb0\xba\xe5\xaf\xb8'), (1, b'M\xe5\xb0\xba\xe5\xaf\xb8'), (2, b'L\xe5\xb0\xba\xe5\xaf\xb8'), (3, b'XL\xe5\xb0\xba\xe5\xaf\xb8')])),
                ('colors', models.IntegerField(default=0, verbose_name='\u989c\u8272', choices=[(0, b'\xe9\xbb\x91\xe8\x89\xb2'), (1, b'\xe7\x99\xbd\xe8\x89\xb2'), (2, b'\xe7\xbb\xbf\xe8\x89\xb2'), (3, b'\xe9\xbb\x84\xe8\x89\xb2')])),
                ('openid', models.CharField(max_length=200)),
                ('printcode', models.CharField(max_length=200, null=True, verbose_name='\u6253\u5370\u78bc', blank=True)),
                ('isprint', models.IntegerField(default=1, verbose_name='\u6253\u5370\u72b6\u6001', choices=[(0, b'\xe5\xb7\xb2\xe6\x89\x93\xe5\x8d\xb0'), (1, b'\xe6\x9c\xaa\xe6\x89\x93\xe5\x8d\xb0')])),
                ('workid', models.CharField(max_length=100, verbose_name='\u7f16\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='\u94fe\u63a5')),
                ('platform', models.IntegerField(verbose_name='\u5e73\u53f0\u7c7b\u578b', choices=[(0, '\u684c\u9762'), (10, '\u5fae\u4fe1')])),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP\u5730\u5740', blank=True)),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5206\u4eab\u8bb0\u5f55',
                'verbose_name_plural': '\u5206\u4eab\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='UniqueVisitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='\u94fe\u63a5')),
                ('ip', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': 'UV',
                'verbose_name_plural': 'UV',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.IntegerField(verbose_name='\u5e73\u53f0\u7c7b\u578b', choices=[(0, '\u684c\u9762'), (10, '\u5fae\u4fe1')])),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP\u5730\u5740', blank=True)),
                ('fixstatus', models.IntegerField(verbose_name='\u5df2\u5b8c\u6210', choices=[(1, b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90'), (0, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6295\u7968\u8bb0\u5f55',
                'verbose_name_plural': '\u6295\u7968\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='VoteCheat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=100, verbose_name='\u5907\u6ce8')),
                ('type', models.IntegerField(verbose_name='\u7c7b\u578b', choices=[(0, b'\xe5\x85\xa8\xe4\xbd\x93\xe5\x88\xb7\xe7\xa5\xa8'), (10, b'\xe5\x8d\x95\xe4\xb8\xaa\xe4\xbd\x9c\xe5\x93\x81\xe5\x88\xb7\xe7\xa5\xa8')])),
                ('minute', models.IntegerField(verbose_name='\u82b1\u8d39\u65f6\u95f4\uff08\u5206\u949f\uff09')),
                ('totalCount', models.IntegerField(verbose_name='\u603b\u91cf')),
                ('nowCount', models.IntegerField(default=0, null=True, verbose_name='\u73b0\u5728\u7684\u91cf', blank=True)),
                ('ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP\u5730\u5740')),
                ('hasFinished', models.BooleanField(default=False, verbose_name='\u5df2\u7ecf\u5b8c\u6210')),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5237\u7968\u4efb\u52a1',
                'verbose_name_plural': '\u5237\u7968\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='WXUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name='\u57ce\u5e02', blank=True)),
                ('gender', models.IntegerField(verbose_name='\u6027\u522b', choices=[(0, b'\xe4\xbf\x9d\xe5\xaf\x86'), (10, b'\xe7\x94\xb7\xe6\x80\xa7'), (20, b'\xe5\xa5\xb3\xe6\x80\xa7')])),
                ('fixstatus', models.IntegerField(verbose_name='\u5df2\u5b8c\u6210', choices=[(1, b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90'), (0, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('comment', models.CharField(max_length=100, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u7528\u6237',
                'verbose_name_plural': '\u5fae\u4fe1\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='YQWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ImageFront', models.CharField(max_length=100000, verbose_name='\u6b63\u9762')),
                ('ImageBack', models.CharField(max_length=100000, verbose_name='\u80cc\u9762')),
                ('ImageSBack', models.ImageField(upload_to=b'', verbose_name='\u80cc\u9762')),
                ('ImageSFront', models.ImageField(upload_to=b'', verbose_name='\u5c0f\u6b63')),
                ('fixstatus', models.IntegerField(verbose_name='\u5df2\u5b8c\u6210', choices=[(1, b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90'), (0, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('creationTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('votedCount', models.IntegerField(default=0, verbose_name='\u83b7\u5f97\u6295\u7968\u6570')),
                ('openid', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='votecheat',
            name='work',
            field=models.ForeignKey(verbose_name='\u4f5c\u54c1\u4fe1\u606f', blank=True, to='yiquan.YQWork', null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='work',
            field=models.ForeignKey(verbose_name='\u4f5c\u54c1\u4fe1\u606f', to='yiquan.YQWork'),
        ),
        migrations.AddField(
            model_name='vote',
            name='wxUser',
            field=models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', blank=True, to='yiquan.WXUser', null=True),
        ),
        migrations.AddField(
            model_name='uniquevisitor',
            name='wxUser',
            field=models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', blank=True, to='yiquan.WXUser', null=True),
        ),
        migrations.AddField(
            model_name='share',
            name='work',
            field=models.ForeignKey(verbose_name='\u4f5c\u54c1\u4fe1\u606f', blank=True, to='yiquan.YQWork', null=True),
        ),
        migrations.AddField(
            model_name='share',
            name='wxUser',
            field=models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', blank=True, to='yiquan.WXUser', null=True),
        ),
    ]
