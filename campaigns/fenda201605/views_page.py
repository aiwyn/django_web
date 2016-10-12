# -*- coding: utf-8 -*-
from campaigns.fenda201605.applet.decorators import page_render, auth_verification, pv
from campaigns.fenda201605.config import ViewConfig
from campaigns.fenda201605.applet.Get_Auth_verification import _Auth_view


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "index.html")
def pc_page_index(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "tidbits.html")
def pc_page_tidbits(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "works.html")
def pc_page_works(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "make.html")
def pc_page_make(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "upload.html")
def pc_page_upload(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "details.html")
def pc_page_details(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def mobile_page_index(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "tidbits.html")
def mobile_page_tidbits(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "details.html")
def mobile_page_details(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "make.html")
def mobile_page_make(request):
    pass

@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "winners.html")
def mobile_result_active(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "winners.html")
def pc_result_active(request):
    pass



@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "resulted.html")
def mobile_page_resulted(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "tidbits_open.html")
def mobile_page_tidbits_open(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "uploadPro.html")
def mobile_page_upload_pro(request):
    pass


@pv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "works.html")
def mobile_page_works(request):
    pass

@_Auth_view
def test_page_works(request):
    return HttpResponse("SUCCESS")
