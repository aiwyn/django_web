from campaigns.testproject.config import ViewConfig
from campaigns.testproject.applet.decorators import page_render


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "index.html")
def index(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "login.html")
def login(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "register.html")
def register(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "lottery.html")
def lottery(request):
    pass

@page_render(ViewConfig.TEMPLATE_PC_URL + "editor.html")
def editor(request):
    pass