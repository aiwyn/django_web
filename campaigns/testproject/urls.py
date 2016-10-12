from django.conf.urls import include, url
from campaigns.testproject import views_action, views_page


urlpatterns = [
    url(r'^login$', views_action.Login),
    url(r'^register', views_action.Register),
    url(r'^signed$', views_action.signed),
    url(r'^center$', views_action.usercenter),
    url(r'^index$', views_page.index),
    url(r'^activelogin$', views_page.login),
    url(r'^activeregister$', views_page.register),
    url(r'^cancellation$', views_action.Cancellation),
    url(r'^index', views_page.index),
    url(r'^cache', views_action.Lottery_Cache),
    url(r'^lottery', views_page.lottery),
    url(r'^myprizes', views_action.myprizes),
    url(r'^test$', views_action.Udiet),
    url(r'^editor$', views_page.editor),
]

