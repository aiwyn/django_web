# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from campaigns.yh import views_page, views_action


urlpatterns = [
    url(r'^upload', views_action.upload),
    url(r'^dream', views_action.fetch_dream),
    url(r'^vote', views_action.dreamVote),
    url(r'^getSignPackage$', views_action.get_sign_package),
    url(r'^self', views_action.fetch_self),
    url(r'^usrdata', views_action.finish),
    url(r'^puv', views_action.exportExcel),
    url(r'^tocould', views_action.tocloud),
    url(r'^random', views_action.random_dream),
    url(r'^index', views_page.index)
]
