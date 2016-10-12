# -*- coding: utf-8 -*-
from campaigns.qiche.applet.decorators import page_render, auth_verification, pv
from campaigns.qiche.config import ViewConfig
from campaigns.qiche.applet.Get_Auth_verification import _Auth_view

@page_render(ViewConfig.TEMPLATE_PC_URL + "index.html")
def index(request):
    pass

@page_render(ViewConfig.TEMPLATE_PC_URL + "lt.html")
def lt(request):
    pass

@page_render(ViewConfig.TEMPLATE_PC_URL + "history.html")
def history(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def ticaindex(request):
    pass

@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "about.html")
def ticaiabout(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "indexSuccess.html")
def ticaisuccess(request):
    pass