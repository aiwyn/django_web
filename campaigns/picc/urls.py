# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from campaigns.picc import views_page, wxviews, views_action

urlpatterns = [
    url(r'^index', views_page.index),
    url(r'^vote', views_action.vote),
    url(r'^dream', views_action.random),
    url(r'^list', views_page._list),
    url(r'^main', views_page._main),
    url(r'^footer', views_page.footer),
    url(r'^get_sign_package', views_action.get_sign_package),
    url(r'^show', views_page.show)
]
