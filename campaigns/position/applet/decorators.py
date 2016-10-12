# -*- coding: utf-8 -*-
import json, time
from django import http
from campaigns.foundation.const import DisplayConst, FoundationConst
from campaigns.foundation.applet import utils, response, access


def _record_pv_uv(request, app_id):
    creation_time = int(time.time())
    url = request.path
    ip = utils.get_ip_from_request(request)
    rs = access.redis_session()
    # pv
    list_name = '{0}:{1}'.format(FoundationConst.REDIS_LIST_PV, app_id)
    value = {FoundationConst.RN_URL: url, FoundationConst.RN_CREATION_TIME: creation_time, FoundationConst.RN_IP: ip}
    rs.rpush(list_name, json.dumps(value))
    # uv
    wx_openid = request.COOKIES.get(FoundationConst.PLATFORM_WEIXIN_NAME)
    if wx_openid is not None:
        list_name = '{0}:{1}'.format(FoundationConst.REDIS_LIST_UV, app_id)
        value = {FoundationConst.PLATFORM_WEIXIN_NAME: wx_openid, FoundationConst.RN_URL: url, FoundationConst.RN_CREATION_TIME: creation_time, FoundationConst.RN_IP: ip}
        rs.rpush(list_name, json.dumps(value))


def _render_page(request, template_name, other_dict_data, page_view, *args, **kwargs):
    try:
        rd = page_view(request, *args, **kwargs)
        cookie_list = utils.get_cookie_list_from_request(request)
        if isinstance(rd, dict):
            if other_dict_data is not None:
                rd.update(other_dict_data)
            return response.page_success(template_name, rd, cookie_list)
        elif rd is None:
            return response.page_success(template_name, other_dict_data, cookie_list)
        elif isinstance(rd, http.HttpResponse):
            return rd
        else:
            raise utils.ServerException(DisplayConst.EXCEPTION_SERVER_NOT_STD_BEHAVIOUR)
    except Exception as e:
        client_error_dict = {DisplayConst.ERROR_MESSAGE: str(e)}
        if isinstance(e, utils.ClientException):
            return response.page_400(DisplayConst.PAGE_400, client_error_dict)
        elif isinstance(e, utils.ServerException):
            return response.page_500(DisplayConst.PAGE_500, client_error_dict)
        else:
            return response.page_501(DisplayConst.PAGE_501, client_error_dict)


def _render_action(request, action_view, *args, **kwargs):
    try:
        rd = action_view(request, *args, **kwargs)
        cookie_list = utils.get_cookie_list_from_request(request)
        if isinstance(rd, dict):
            return response.action_success(rd, cookie_list)
        elif rd is None:
            return response.action_success(dict(), cookie_list)
        elif isinstance(rd, http.HttpResponse):
            return rd
        else:
            raise utils.ServerException(DisplayConst.EXCEPTION_SERVER_NOT_STD_BEHAVIOUR)
    except Exception as e:
        client_error_dict = {DisplayConst.ERROR_MESSAGE: str(e)}
        if isinstance(e, utils.ClientException):
            return response.action_400(client_error_dict)
        elif isinstance(e, utils.ServerException):
            return response.action_500(client_error_dict)
        else:
            return response.action_501(client_error_dict)

