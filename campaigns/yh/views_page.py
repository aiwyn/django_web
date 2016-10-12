# -*- coding: utf-8 -*-
from campaigns.yh.applet.decorators import page_render, auth_verification, pv
from campaigns.yh.config import ViewConfig
from campaigns.yh.applet.Get_Auth_verification import _Auth_view


@pv
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def index(request):
    pass
