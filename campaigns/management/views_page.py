from campaigns.management.config import ViewConfig
from campaigns.management.applet.decorators import page_render


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def index(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "login.html")
def login(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "register.html")
def register(request):
    pass


