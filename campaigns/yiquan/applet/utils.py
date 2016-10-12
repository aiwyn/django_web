# -*- coding: utf-8 -*-
import os, uuid, datetime, time, StringIO
from PIL import Image
from campaigns.foundation.const import FoundationConst
from campaigns.yiquan.config import ViewConfig, WorkConfig
from cmp import settings
from campaigns.yiquan import models
def generate_other_dict_data():
    odd = dict()
    odd[FoundationConst.RN_STATIC_URL] = '{0}{1}'.format(settings.STATIC_URL, ViewConfig.STATIC_URL)
    if settings.DEBUG:
        odd[FoundationConst.RN_WEIXIN_DEBUG] = '?{0}'.format(int(time.time()))
    return odd


# 为上传图片指定路径
def handle_image_upload(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper


class ClientException(Exception):
    def __init__(self, msg, detail_msg=None):
        self.msg = msg
        self.detail_msg = detail_msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg if self.detail_msg is None else self.detail_msg


class ServerException(Exception):
    def __init__(self, msg, detail_msg=None):
        self.msg = msg
        self.detail_msg = detail_msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg if self.detail_msg is None else self.detail_msg


def get_ip_from_request(request):
    if request.META.has_key(FoundationConst.DJANGO_HTTP_X_FORWARDED_FOR):
        return request.META[FoundationConst.DJANGO_HTTP_X_FORWARDED_FOR]
    else:
        return request.META[FoundationConst.DJANGO_REMOTE_ADDR]


def put_cookie_to_request(request, cookie_dict):
    if not hasattr(request, FoundationConst.RN_REQUEST_CUSTOM):
        request.CUSTOM = dict()
        request.CUSTOM[FoundationConst.RN_COOKIE_LIST] = [cookie_dict, ]
    else:
        request.CUSTOM[FoundationConst.RN_COOKIE_LIST].append(cookie_dict)


def get_cookie_list_from_request(request):
    cookie_list = None
    if hasattr(request, FoundationConst.RN_REQUEST_CUSTOM):
        cookie_list = request.CUSTOM.get(FoundationConst.RN_COOKIE_LIST, None)
    return cookie_list


def put_dict_data_to_request(request, key, value):
    if not hasattr(request, FoundationConst.RN_REQUEST_CUSTOM):
        request.CUSTOM = dict()
    request.CUSTOM[key] = value


def generate_uuid():
    return uuid.uuid4().hex

def fit_up_works(PrintWork):
    dict_work = dict()
    dict_work['openid'] = PrintWork.openid
    dict_work['workId'] = PrintWork.workid
    dict_work['AuthorSize'] = PrintWork.size
    dict_work['AuthorColors'] = PrintWork.colors
    dict_work['AuthorCode'] = PrintWork.printcode
    INFO = models.YQWork.objects.filter(id=PrintWork.workid).first()
    if INFO is None:
        dict_work['Fix_Status'] = 0
    else:
        dict_work['workfrontUrl'] = INFO.ImageSFront.url
        dict_work['workCreationTime'] = (INFO.creationTime + datetime.timedelta(hours=8)).strftime(FoundationConst.EXPORT_DATETIME_MINUTE_FORMAT)
        dict_work['top'] = models.YQWork.objects.filter(votedCount__gt=INFO.votedCount).count() + 1
        dict_work['workVotedCount'] = INFO.votedCount
        dict_work['isRelation'] = 1
        dict_work['Fix_Status'] = INFO.fixstatus
    return dict_work

def fit_up_work_lists(work_list):
    dict_work_lists = list()
    for work in work_list:
        dict_work = fit_up_works(work)
        if dict_work['Fix_Status'] == 0:
            dict_work_lists.append(dict_work)
    return dict_work_lists



def fit_up_work(YQwork):
    dict_work = dict()
    dict_work['openid'] = YQwork.openid
    dict_work['workId'] = YQwork.id
    dict_work['workfrontUrl'] = YQwork.ImageSFront.url
    dict_work['workbackUrl'] = YQwork.ImageSBack.url
    dict_work['workVotedCount'] = YQwork.votedCount
    dict_work['workCreationTime'] = (YQwork.creationTime + datetime.timedelta(hours=8)).strftime(FoundationConst.EXPORT_DATETIME_MINUTE_FORMAT)
    dict_work['Fix_Status'] = YQwork.fixstatus
    dict_work['isRelation'] = 1

    # 查询排名
    dict_work['top'] = models.YQWork.objects.filter(votedCount__gt=YQwork.votedCount).count() + 1

    INFO = models.PrintWork.objects.filter(openid=YQwork.openid, workid=YQwork.id)

    if len(INFO):
        dict_work['AuthorSize'] = INFO[0].size
        dict_work['AuthorColors'] = INFO[0].colors
        dict_work['AuthorCode'] = INFO[0].printcode
    else:
        dict_work['AuthorSize'] = 1
        dict_work['AuthorColors'] = 1
        dict_work['AuthorCode'] = "000000"
    return dict_work


def fit_up_work_list(work_list):
    dict_work_list = list()
    for work in work_list:
        dict_work = fit_up_work(work)
        dict_work_list.append(dict_work)
    return dict_work_list


def save_work_image(http_chunk):
    filename = http_chunk.name.encode(FoundationConst.ENCODE_UTF8)
    if filename == 'blob':
        filename = 'blob.png'
    mem_file = StringIO.StringIO()
    for chunk in http_chunk.chunks():
        mem_file.write(chunk)
    image = Image.open(mem_file)
    ext = filename.split('.')[-1]
    filename = '{0}{1}.{2}'.format(WorkConfig.REL_PATH_IMAGE, uuid.uuid4().hex, ext)
    image.save(settings.MEDIA_ROOT + filename)
    return filename

