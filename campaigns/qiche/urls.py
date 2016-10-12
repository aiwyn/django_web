from django.conf.urls import include, url
from campaigns.qiche import views_page, views_action

urlpatterns = [
      url(r'^recv', views_action.revcdata),
      url(r'^index', views_page.index),
      url(r'^lt', views_page.lt),
      url(r'^history', views_page.history),
      url(r'^main/index.html$', views_page.ticaindex),
      url(r'^main/about.html$', views_page.ticaiabout),
      url(r'^main/indexSuccess.html$', views_page.ticaisuccess)
      ]