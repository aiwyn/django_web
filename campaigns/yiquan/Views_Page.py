from campaigns.yiquan.applet.decorators import pv, P_verify_auth, page_render
from campaigns.yiquan.config import ViewConfig


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "pc-index.html")
def pc_page_index(request):
    pass

@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "pc-product.html")
def pc_page_product(request):
    pass


@pv
@page_render(ViewConfig.TEMPLATE_PC_URL + "pc-news.html")
def pc_page_news(request):
    pass


@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-infinite.html")
def shuazuoping(request):
    pass


@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-index.html")
def mobile_page_index(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-index2.html")
def mobile_page_index2(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-activeIndex.html")
def mobile_page_activeIndex(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-make.html")
def mobile_page_make(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-makeSuccess.html")
def mobile_page_makeSuccess(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-mark.html")
def mobile_page_mark(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-myProduct.html")
def mobile_page_myproduct(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-nav.html")
def mobile_page_nav(request):
    pass

@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-otherProduct.html")
def mobile_page_other(request):
    pass


@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-product.html")
def mobile_page_product(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-tidbits.html")
def mobile_page_tidbits(request):
    pass


@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-weMake.html")
def mobile_page_wemake(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-weMakeSeed.html")
def mobile_page_makeseed(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-weMakeShare.html")
def mobile_page_share(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-weMakeShare1.html")
def mobile_page_Share(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-weMakeShareEnd.html")
def mobile_page_ShareEnd(request):
    pass

@pv
@P_verify_auth
@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "wx-index.html")
def auth_test(request):
    pass

@page_render(ViewConfig.TEMPLATE_MOBILE_URL + "error.html")
def Page_Error(request):
    pass