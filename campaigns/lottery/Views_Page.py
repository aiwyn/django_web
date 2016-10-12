from campaigns.lottery.config import ViewConfig
from campaigns.lottery.applet.decorators import page_render


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "lottery.html")
def index(request):
    pass


