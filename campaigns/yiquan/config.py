# -*- coding: utf-8 -*-


class WorkConfig(object):
    # relative path
    REL_PATH_IMAGE = 'campaigns/yiquan/work/image'


class VoteConfig(object):
    IP_LIMIT_COUNT = 5
    WEIXIN_LIMIT_COUNT = 5


class ViewConfig(object):
    STATIC_URL = 'campaigns/yiquan/'
    TEMPLATE_URL = 'yiquan/'
    TEMPLATE_PC_URL = TEMPLATE_URL + 'pc/'
    TEMPLATE_MOBILE_URL = TEMPLATE_URL + 'mobile/'


class RegenerateConfig(object):
    KIT_ABS_PATH = '/www/project/imagedir/'
    RAW_CANVAS_WIDTH = 450
    RAW_CANVAS_HEIGHT = 636
    DES_CANVAS_WIDTH = 3508
    DES_CANVAS_HEIGHT = 4961
    BIG_WORK_IMAGE_FILE_PATH = '/tmp/'
