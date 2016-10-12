# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from campaigns.fenda201605 import views_page, wxviews, views_action, views

urlpatterns = [
    url(r'^index.html', views.index),
    url(r'^wxindex.html/$', wxviews.index),

    url(r'^   ', views_page.pc_page_index),
    url(r'^pc/tidbits.html$', views_page.pc_page_tidbits),
    url(r'^pc/works.html$', views_page.pc_page_works),
    url(r'^pc/make.html$', views_page.pc_page_make),
    url(r'^pc/upload.html$', views_page.pc_page_upload),
    url(r'^pc/details.html', views_page.pc_page_details),

    url(r'^pc/uploadPhotoWork$', views_action.pc_upload_photo_work),
    url(r'^pc/uploadDIYWork$', views_action.pc_upload_diy_work),
    url(r'^pc/fetchWorks$', views_action.pc_fetch_works),
    url(r'^pc/fetchWork$', views_action.pc_fetch_work),
    url(r'^pc/vote$', views_action.pc_vote),

    url(r'^mobile/index.html', views_page.mobile_page_index),
    url(r'^mobile/tidbits.html', views_page.mobile_page_tidbits),
    url(r'^mobile/details.html', views_page.mobile_page_details),
    url(r'^mobile/make.html', views_page.mobile_page_make),
    url(r'^mobile/activeresult$', views_page.mobile_result_active),
    url(r'^pc/activeresult$', views_page.pc_result_active),
    url(r'^mobile/resulted.html', views_page.mobile_page_resulted),
    url(r'^mobile/tidbits_open.html', views_page.mobile_page_tidbits_open),
    url(r'^mobile/uploadPro.html', views_page.mobile_page_upload_pro),
    url(r'^mobile/works.html', views_page.mobile_page_works),
    url(r'^mobile/test.html', views_page.test_page_works),

    url(r'^mobile/uploadPhotoWork$', views_action.pc_upload_photo_work),
    url(r'^mobile/uploadDIYWork$', views_action.pc_upload_diy_work),
    url(r'^mobile/fetchWorks$', views_action.pc_fetch_works),
    url(r'^mobile/fetchWork$', views_action.pc_fetch_work),
    url(r'^mobile/vote$', views_action.pc_vote),

    url(r'^mobile/mobile_share$', views_action.mobile_share),
    url(r'^mobile/getSignPackage$', views_action.get_sign_package),
    url(r'^test$', views_action.upload_test),
]
