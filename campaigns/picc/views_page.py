# -*- coding: utf-8 -*-
from campaigns.picc.applet.decorators import page_render, auth_verification, pv, uv
from campaigns.picc.config import ViewConfig


@pv
@uv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def index(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "show.html")
def show(request):
    pass



@pv
@uv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "list.html")
def _list(request):
    pass


@pv
@uv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "main.html")
def _main(request):
    pass


@pv
@uv
@auth_verification
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "footer.html")
def footer(request):
    pass

