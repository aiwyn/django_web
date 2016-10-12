# -*- coding: utf-8 -*-
from campaigns.nihuawocai.applet.decorators import page_render
from campaigns.nihuawocai.config import ViewConfig

@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def index(request):
    pass