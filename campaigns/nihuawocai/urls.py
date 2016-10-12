# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from campaigns.nihuawocai import views_page, views_actions, views


urlpatterns = [
    url(r'^login', views_actions.Userlogin),
    url(r'^answer', views_actions.GetAnswer),
    url(r'^join', views_actions.joingame),
    url(r'^index', views_page.index),
    url(r'^start', views_actions.StartWebsocket),
    ]
