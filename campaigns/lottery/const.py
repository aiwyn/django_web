# -*- coding: utf-8 -*-


class WXUserConst(object):
    # verbose name
    VN_TABLE_NAME = u'微信用户'


class AuthorConst(object):
    # verbose name
    VN_TABLE_NAME = u'作者信息'


class WorkConst(object):
    # verbose name
    VN_TABLE_NAME = u'作品信息'
    TYPE_PHOTO = 0
    TYPE_DIY = 10
    TYPE_CHOICES = (
        (TYPE_PHOTO, '拍照上传'),
        (TYPE_DIY, '线上制作'),
    )
    # short_description
    SD_IMAGE_TAG = '作品预览'
    SD_FETCH_WORK_IMAGE_TAG = '获取作品照片'
    TAG_FETCH_WORK_IMAGE = '<div><a href="/yiquan/fetch_front_image?workId={0}">获取正面大图片</a><a href="/yiquan/fetch_back_image?workId={0}">获取背面大图片</a></div>'
    SHOW_NAME_FRONT_IMAGE = 'front.png'
    SHOW_NAME_BACK_IMAGE = 'back.png'


class ShareConst(object):
    # verbose name
    VN_TABLE_NAME = u'分享记录'


class TimeConst(object):
    VN_TABLE_NAME = u'抽奖活动信息表'


class InfoConst(object):
    VN_TABLE_NAME = u'奖品放出时间表'


class PrizesConst(object):
    VN_TABLE_NAME = u'奖品池'


class VoteConst(object):
    # verbose name
    VN_TABLE_NAME = u'投票记录'


class UsrConst(object):
    VN_TABLE_NAME = u'中奖人信息'


class VoteCheatConst(object):
    # verbose name
    VN_TABLE_NAME = u'刷票任务'
    TYPE_ALL = 0
    TYPE_ONE = 10
    TYPE_CHOICES = (
        (TYPE_ALL, '全体刷票'),
        (TYPE_ONE, '单个作品刷票'),
    )


class PageViewConst(object):
    # verbose name
    VN_TABLE_NAME = u'PV'


class UniqueVisitorConst(object):
    # verbose name
    VN_TABLE_NAME = u'UV'


class ViewConst(object):
    RN_AUTHOR_SIZE = 'AuthorSize'
    RN_AUTHOR_COLORS = 'AuthorColors'
    RN_WORK_IMAGE_FRONT = 'workImageFront'
    RN_WORK_IMAGE_BACK = 'workImageBack'
    RN_WORK_IMAGE_SFRONT = 'workImageSFront'
    RN_WORK_IMAGE_SBACK = 'workImageSBack'
    RN_WORK_ID = 'workId'
    RN_OPEN_ID = 'openid'
    RN_CODE = 'AuthorCode'
    RN_VOTE = "vote"
    RN_TOP = 'top'
    RN_USRID = 'userid'
    RN_NICKNAME = 'nickname'
    FIX_STATUS = 'Fix_Status'
    CLIENT_EXCEPTION_PRINT_STATUS = 'PrintStatus'
    FIX = '已完成'
    UNFIX = '未完成'
    RN_NAME = 'usrname'
    RN_ACTIVEID = 'activeid'
    RN_NUMBER = 'usrnum'
    RN_ADDRESS = 'usraddr'
    RN_PRIZES = 'hitprizes'
    RN_PRID = 'prizesid'
    RN_SCODE = 'result_code'
    RN_SMSG = 'result_msg'
    RN_PRIZESLVL = 'prizeslvl'