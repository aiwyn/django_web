#encoding=utf-8
from campaigns.fenda201605.applet import decorators
from campaigns.lottery import const, models
from campaigns.foundation.const import FoundationConst, DisplayConst
from django.http import HttpResponse
import random, time


#  用户信息表
@decorators.action_render
def userinfo(request):
    userinfo = request.POST[const.ViewConst.RN_NAME]
    usernumber = request.POST[const.ViewConst.RN_NUMBER].encode(FoundationConst.ENCODE_UTF8)
    # usrid = request.session.get(const.ViewConst.RN_USRID)
    usrid = '咩哈哈哈哈哈'
    useraddress = request.POST[const.ViewConst.RN_ADDRESS]
    userlevel = int(request.POST[const.ViewConst.RN_PRIZESLVL])
    userprizes = (request.POST[const.ViewConst.RN_PRIZES]).encode(FoundationConst.ENCODE_UTF8)
    userprid = int(request.POST[const.ViewConst.RN_PRID])
    userdata = models.lottery_info.objects.create(
        usrname=userinfo,
        usernum=usernumber,
        usraddr=useraddress,
        lottinfo=userlevel,
        userid=usrid,
        prid=userprid,
        prizesname=userprizes
    )


@decorators.action_render
def Lottery_Cache(request):
    ActiveId = request.POST[const.ViewConst.RN_ACTIVEID]
    _Much = random.randint(1, 1000000)
    # usrinfo = request.POST[const.ViewConst.RN_USRID]
    usrinfo = "肮脏的奇奇"
    _nowtime = int(time.time())
    try:
        _Activeid = models.activetime.objects.get(id=ActiveId)
        starttime = int(time.mktime(time.strptime(str(_Activeid.starttime), "%Y-%m-%d")))
        stoptime = int(time.mktime(time.strptime(str(_Activeid.stoptime), "%Y-%m-%d")))
    except Exception as e:
        return HttpResponse(e)

    if _nowtime > starttime and _nowtime < stoptime:
        # random用户获奖资格
        if _Much <= int(_Activeid.chance * 10000):
            _time = int(time.time())
            try:
                # 匹配当前时间奖品池剩余奖品
                _prizes = models.Lottery_prizes.objects.filter(activetime__lte=_time, activeid=ActiveId, isdole=1).all()
                if _prizes:
                    l1 = []
                    for i in _prizes:
                        l1.append(i.id)
                    _length = random.randint(1, int(len(l1)))                                   # 得出奖品列表随机数
                    _prid = l1[_length - 1]
                    hitprize = models.Lottery_prizes.objects.get(id=_prid)
                    _hitprizes = models.Lottery_prizes.objects.filter(id=_prid).update(isdole=0, userid=usrinfo)
                    return {const.ViewConst.RN_PRIZESLVL: hitprize.prizeslvl, const.ViewConst.RN_PRIZES: hitprize.prizesname, const.ViewConst.RN_PRID: hitprize.id, const.ViewConst.RN_SCODE: 0, const.ViewConst.RN_SMSG: None}
                else:
                    return {const.ViewConst.RN_PRIZESLVL: 0, const.ViewConst.RN_PRIZES: None, const.ViewConst.RN_PRID: None, const.ViewConst.RN_SCODE: 0, const.ViewConst.RN_SMSG: None}
            except Exception as e:
                return HttpResponse(e)
        else:
            return {const.ViewConst.RN_PRIZESLVL: 0, const.ViewConst.RN_PRIZES: None, const.ViewConst.RN_PRID: None, const.ViewConst.RN_SCODE: 0, const.ViewConst.RN_SMSG: None}
    elif _nowtime <= starttime:
        return {"result_code": 1, "result_msg": "活动未开始"}
    elif _nowtime >= stoptime:
        return {"result_code": 2, "result_msg": "活动已结束"}




# 后台活动表
@decorators.action_render
def activetime(request):
    activename = request.POST['activename'].encode[FoundationConst.ENCODE_UTF8]
    chance = float(request.POST['chance'])
    starttime = request.POST['starttime']
    stoptime = request.POST['stoptime']
    __Activedays = int(time.mktime(time.strptime(stoptime, "%Y-%m-%d"))) - int(time.mktime(time.strptime(starttime, "%Y-%m-%d")))
    activedays = __Activedays / 3600 / 24
    ucount = request.POST['ucount']
    dcount = request.POST['dcount']
    activeInfo = models.activetime.objects.create(
        activename=activename,
        chance=chance,
        starttime=starttime,
        stoptime=stoptime,
        activedays=activedays,
        ucount=ucount,
        dcount=dcount,
    )
    return {const.ViewConst.RN_SCODE: 0, const.ViewConst.RN_SMSG: None, const.ViewConst.RN_ACTIVEID: activeInfo.id}


# 后台activeinfo表单存入数据库 并批量插入奖品池
@decorators.action_render
def activeinfo(request):
    INFO = int(request.POST[const.ViewConst.RN_ACTIVEID])
    activeInfo = models.activetime.objects.get(id=INFO)                         # 匹配相应活动ID奖品信息
    count = 1
    while count < int(activeInfo.activedays):                                  # 活动总天数测算表单行数
        a = "active" + str(count)
        info = request.POST[a]
        if info is not None:
            prizeslvl = int(info["prizeslvl"])
            quantity = int(info["quantity"])
            prizesname = info["prizesname"].encode(FoundationConst.ENCODE_UTF8)
            releasedate = info["releasedate"].encode(FoundationConst.ENCODE_UTF8)
            activetime = models.activeinfo.objects.create(
                activeId=activeInfo.id,
                prizesname=prizesname,
                prizeslvl=prizeslvl,
                quantity=quantity,
                releasedate=releasedate,
            )
            count = int(count) + 1
        else:
            count = int(count) + 1
            continue

    # 信息存入后台奖品池
    __active = models.activeinfo.objects.filter(activeId=INFO).all()
    if __active is not None:
        for work in __active:
            count = 1
            while count < work.quantity:
                _addlottery = models.Lottery_prizes.objects.create(
                    prizeslvl=work.prizeslvl,
                    isdole=FoundationConst.UNDOLE,
                    userid=None,
                    activeid=activeInfo.id,
                    prizesname=work.prizesname,
                    activetime=time.mktime(time.strptime(work.releasedate, "%Y-%m-%d"))
                )
                count = int(count) + 1
        return {const.ViewConst.RN_SCODE: 0, const.ViewConst.RN_SMSG: "SUCCESS"}
    else:
        return {const.ViewConst.RN_SCODE: 1, const.ViewConst.RN_SMSG: "更新数据表单失败"}

