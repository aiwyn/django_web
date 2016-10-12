from django.conf.urls import include, url
from campaigns.lottery import Views_Action, Views_Page

urlpatterns = [
    url(r'^index', Views_Page.index),
    url(r'^cache', Views_Action.Lottery_Cache),
    url(r'^userinfo', Views_Action.userinfo),
    url(r'^activetime$', Views_Action.activetime),
    url(r'^activeinfo$', Views_Action.activeinfo),
]