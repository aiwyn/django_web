# -*- coding: utf-8 -*-
import time
import random
from campaigns.testproject.applet import decorators, utils
from campaigns.testproject import models, const
from django.http import HttpResponse



@decorators.action_render
def Lottery_Cache(request):
    usrid = request.session.get(const.management.VN_USR_ID)
    if usrid is None:
        return {"result_code": 3, "result_msg": "尚未登录请先登录"}
    else:
        usrpoint = request.session.get(const.management.VN_USR_POINT)
        if int(usrpoint) == 1:
            request.session[const.management.VN_USR_POINT] = 0
            ActiveId = request.POST[const.ViewConst.RN_ACTIVEID]
            _Much = random.randint(1, 1000000)
            # usrinfo = request.POST[const.ViewConst.RN_USRID]
            usrinfo = models.Mangers.objects.filter(id=usrid).first()
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
                        _prizes = models.prizes.objects.filter(activetime__lte=_time, activeid=ActiveId, isdole=1).all()
                        if _prizes:
                            l1 = []
                            for i in _prizes:
                                l1.append(i.id)
                            _length = random.randint(1, int(len(l1)))                                   # 得出奖品列表随机数
                            _prid = l1[_length - 1]
                            hitprize = models.prizes.objects.get(id=_prid)
                            _hitprizes = models.prizes.objects.filter(id=_prid).update(isdole=0, userid=usrid)
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
        elif int(usrpoint) == 0:
            usrinfo = models.Mangers.objects.filter(id=usrid).first()
            if int(usrinfo.point) < 1:
                return {"result_code": 1, "result_msg": "您的积分不够"}
            else:
                lastpoint = int(usrinfo.point) - 1
                usrinfo = models.Mangers.objects.filter(id=usrid).update(point=lastpoint)
                ActiveId = request.POST[const.ViewConst.RN_ACTIVEID]
                _Much = random.randint(1, 1000000)
                # usrinfo = request.POST[const.ViewConst.RN_USRID]
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
                            _prizes = models.prizes.objects.filter(activetime__lte=_time, activeid=ActiveId,
                                                                   isdole=1).all()
                            if _prizes:
                                l1 = []
                                for i in _prizes:
                                    l1.append(i.id)
                                _length = random.randint(1, int(len(l1)))  # 得出奖品列表随机数
                                _prid = l1[_length - 1]
                                hitprize = models.prizes.objects.get(id=_prid)
                                _hitprizes = models.prizes.objects.filter(id=_prid).update(isdole=0, userid=usrid)
                                return {const.ViewConst.RN_PRIZESLVL: hitprize.prizeslvl,
                                        const.ViewConst.RN_PRIZES: hitprize.prizesname,
                                        const.ViewConst.RN_PRID: hitprize.id, const.ViewConst.RN_SCODE: 0,
                                        const.ViewConst.RN_SMSG: None}
                            else:
                                return {const.ViewConst.RN_PRIZESLVL: 0, const.ViewConst.RN_PRIZES: None,
                                        const.ViewConst.RN_PRID: None, const.ViewConst.RN_SCODE: 0,
                                        const.ViewConst.RN_SMSG: None}
                        except Exception as e:
                            return HttpResponse(e)
                    else:
                        return {const.ViewConst.RN_PRIZESLVL: 0, const.ViewConst.RN_PRIZES: None,
                                const.ViewConst.RN_PRID: None, const.ViewConst.RN_SCODE: 0,
                                const.ViewConst.RN_SMSG: None}
                elif _nowtime <= starttime:
                    return {"result_code": 1, "result_msg": "活动未开始"}
                elif _nowtime >= stoptime:
                    return {"result_code": 2, "result_msg": "活动已结束"}


@decorators.action_render
def myprizes(request):
    try:
        usrid = request.session.get(const.management.VN_USR_ID)
        if usrid is None:
            return {"result_code": 0, "result_msg": "您尚未登录"}
        else:
            prizesinfo = models.prizes.objects.filter(userid=usrid).all()
            prizeslist = list()
            for Myprizes in prizesinfo:
                d1 = dict()
                d1[const.ViewConst.RN_PRIZES] = Myprizes.prizesname
                d1[const.ViewConst.RN_PRIZESLVL] = Myprizes.prizeslvl
                d1[const.ViewConst.RN_PRID] = Myprizes.id
                d1[const.ViewConst.RN_ISDONE] = Myprizes.isdone
                prizeslist.append(d1)
            return {"result_code": 0, "result_msg": "done", const.ViewConst.RN_MYPRIZES: prizeslist}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}


# 用户信息注册
@decorators.action_render
def Register(request):
    try:
        usrname = request.POST[const.management.VN_USR_NAME]
        usradd = request.POST[const.management.VN_USR_ADDR]
        usrnum = request.POST[const.management.VN_USR_NUM]
        usrsex = int(request.POST[const.management.VN_USR_SEX])
        usrpw = request.POST[const.management.VN_USR_PASSWD]
        usrdp = utils.save_work_image(request.FILES[const.management.VN_USR_DISPLAY])
        print usrdp
    except Exception as e:
        return HttpResponse(e)
    Userphonecall = models.Mangers.objects.filter(usrnum=usrnum).first()
    if Userphonecall is None:
        try:
            Register_info = models.Mangers.objects.create(
                name=usrname,
                passwd=usrpw,
                usrnum=usrnum,
                display=usrdp,
                gender=usrsex,
                usraddr=usradd
            )
            Userpoint = models.usrpoint.objects.create(
                info=Register_info,
                datetime=None,
                continuity=None,
                point=0,
            )
            return {const.management.VN_USR_ID: Register_info.id, "result_code": 0, "result_msg": "success"}
        except Exception as e:
            return HttpResponse(e)
    else:
        return {"result_code": 1, "result_msg": "该手机号已被注册"}


# 会员登录接口
@decorators.action_render
def Login(request):
    try:
        usrnum = request.POST[const.management.VN_USR_NUM]
        usrpasswd = request.POST[const.management.VN_USR_PASSWD]
        usrinfo = models.Mangers.objects.get(usrnum=usrnum)
        try:
            UsrInfo = models.Mangers.objects.filter(usrnum=usrnum, passwd=usrpasswd).first()
            if UsrInfo is not None:
                request.session[const.management.VN_USR_ID] = UsrInfo.id
                return {const.management.VN_USR_POINT: UsrInfo.point, const.management.VN_USR_ID: UsrInfo.id, const.management.VN_USR_NAME: UsrInfo.name, const.management.VN_USR_DISPLAY: UsrInfo.display.url, "result_code": 0, "result_msg": "SUCCESS"}
            else:
                return {"result_code": 1, "result_msg": "密码错误"}
        except Exception as e:
            return {"result_code": -1, "result_msg": e}
    except Exception as e:
        return {"result_code": -1, "result_msg": "无此注册用户"}


# 签到接口
@decorators.action_render
def signed(request):
    try:
        usrid = request.session.get(const.management.VN_USR_ID)
        usrinfo = models.usrpoint.objects.filter(info__id=usrid).first()
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}
    nowtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    if usrinfo.datetime is None:
        UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
            datetime=nowtime,
            continuity=1,
            point=int(usrinfo.point) + 1,
        )
        UserActive = models.Mangers.objects.filter(id=usrid).update(
            point=int(usrinfo.point) + 1,
        )
        request.session[const.management.VN_USR_POINT] = 1
        return {"result_code": 0, "result_msg": "签到成功获得1点奖励"}
    else:
        continutly = int(str(nowtime.split("-")[0]) + str(nowtime.split("-")[1]) + str(nowtime.split("-")[2])) - int(str(usrinfo.datetime).split("-")[0] + str(usrinfo.datetime).split("-")[1] + str(usrinfo.datetime).split("-")[2])
        if continutly == 1:
            if 7 > int(usrinfo.continuity) + 1 >= 0:
                UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                    datetime=nowtime,
                    continuity=continutly + 1,
                    point=int(usrinfo.point) + 1,
                )
                UserActive = models.Mangers.objects.filter(id=usrid).update(
                    point=int(usrinfo.point) + 1,
                )
                request.session[const.management.VN_USR_POINT] = 1
                a = "签到成功您已连续签到%s天" % str(continutly+1)
                return {'result_code': 0, "result_msg": a}

            elif int(usrinfo.continuity) + 1 == 7:
                UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                    datetime=nowtime,
                    continuity=continutly + 1,
                    point=int(usrinfo.point) + 5,
                )
                UserActive = models.Mangers.objects.filter(id=usrid).update(
                    point=int(usrinfo.point) + 5,
                )
                request.session[const.management.VN_USR_POINT] = 1
                return {'result_code': 0, "sesult_msg": "签到成功您已连续签到7点获得5点奖励"}

            elif 30 > int(usrinfo.continuity) + 1 > 7:
                UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                    datetime=nowtime,
                    continuity=continutly + 1,
                    point=int(usrinfo.point) + 1,
                )
                UserActive = models.Mangers.objects.filter(id=usrid).update(
                    point=int(usrinfo.point) + 1,
                )
                request.session[const.management.VN_USR_POINT] = 1
                a = "签到成功您已连续签到%s天" % str(int(continutly) + 1)
                return {'result_code': 0, "result_msg": a}

            elif int(usrinfo.continuity) + 1 == 30:
                UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                    datetime=nowtime,
                    continuity=continutly + 1,
                    point=int(usrinfo.point) + 10,
                )
                UserActive = models.Mangers.objects.filter(id=usrid).update(
                    point=int(usrinfo.point) + 10,
                )
                request.session[const.management.VN_USR_POINT] = 1
                return {'result_code': 0, "result_msg": "签到成功您已连续签到30天获得10点奖励"}

            else:
                if int(usrinfo.continuty) + 1 % 30 == 0:
                    UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                        datetime=nowtime,
                        continuity=continutly + 1,
                        point=int(usrinfo.point) + 10,
                    )
                    UserActive = models.Mangers.objects.filter(id=usrid).update(
                        point=int(usrinfo.point) + 10,
                    )
                    request.session[const.management.VN_USR_POINT] = 1
                    a = "签到成功您已连续签到%s个月获得10点奖励" % str(int(usrinfo.continuty) + 1 / 30)
                    return {"result_code": 0, "result_msg": a}
                else:
                    UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                        datetime=nowtime,
                        continuity=continutly + 1,
                        point=int(usrinfo.point) + 1,
                    )
                    UserActive = models.Mangers.objects.filter(id=usrid).update(
                        point=int(usrinfo.point) + 1,
                    )
                    request.session[const.management.VN_USR_POINT] = 1
                    a = "签到成功您已连续签到%s天获得1点奖励" % str(int(usrinfo.continuty) + 1)
                    return {"result_code": 0, "result_msg": a}

        elif continutly == 0:
            return {"result_code": 1, "result_msg": "您今天已经签到过"}

        else:
            UsrInfo = models.usrpoint.objects.filter(info__id=usrid).update(
                datetime=nowtime,
                continuity=1,
                point=int(usrinfo.point) + 1,
            )
            UserActive = models.Mangers.objects.filter(id=usrid).update(
                point=int(usrinfo.point) + 1,
            )
            request.session[const.management.VN_USR_POINT] = 1
            return {"result_code": 0, "result_msg": "签到成功获得1点奖励"}




# 注销
@decorators.action_render
def Cancellation(request):
    usrid = request.session.get(const.management.VN_USR_ID)
    if usrid is None:
        return {"result_code": 2, "result_msg": "您尚未登录"}
    else:
        request.session[const.management.VN_USR_ID] = None
        return {"result_code": 0, "result_msg": "您已退出登录"}



# 用户中心接口
@decorators.action_render
def usercenter(request):
    try:
        usrid = request.session.get(const.management.VN_USR_ID)
        if usrid is None:
            return {"result_code": 2, "result_msg": "您尚未登录"}
        else:
            usrinfo = models.Mangers.objects.filter(id=usrid).first()
            UserActive = models.usrpoint.objects.filter(info__id=usrid).first()
            nowtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if UserActive.datetime is None:
                return {
                    const.management.VN_USR_NAME: usrinfo.name,
                    const.management.VN_USR_DISPLAY: usrinfo.display.url,
                    const.management.VN_USR_NUM: usrinfo.usrnum,
                    const.management.VN_USR_ADDR: usrinfo.usraddr,
                    const.management.VN_USR_POINT: usrinfo.point,
                    const.management.VN_USR_CONTINUE: UserActive.continuity,
                    "result_code": 1,
                    "result_msg": "未签到"
                }
            else:
                continutly = int(str(nowtime.split("-")[0]) + str(nowtime.split("-")[1]) + str(nowtime.split("-")[2])) - int(str(UserActive.datetime).split("-")[0] + str(UserActive.datetime).split("-")[1] +str(UserActive.datetime).split("-")[2])
                if int(continutly) == 0:
                    return {
                        const.management.VN_USR_NAME: usrinfo.name,
                        const.management.VN_USR_DISPLAY: usrinfo.display.url,
                        const.management.VN_USR_NUM: usrinfo.usrnum,
                        const.management.VN_USR_ADDR: usrinfo.usraddr,
                        const.management.VN_USR_POINT: usrinfo.point,
                        const.management.VN_USR_CONTINUE: UserActive.continuity,
                        "result_code": 0,
                        "result_msg": "已签到"
                    }
                else:
                    return {
                        const.management.VN_USR_NAME: usrinfo.name,
                        const.management.VN_USR_DISPLAY: usrinfo.display.url,
                        const.management.VN_USR_NUM: usrinfo.usrnum,
                        const.management.VN_USR_ADDR: usrinfo.usraddr,
                        const.management.VN_USR_POINT: usrinfo.point,
                        const.management.VN_USR_CONTINUE: UserActive.continuity,
                        "result_code": 1,
                        "result_msg": "未签到"
                    }
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}

@decorators.action_render
def Udiet(request):
    Args = request.POST['headline']
    print Args
    data = models.imbatman.objects.filter(headline=Args).first()
    return {'data': data.content, 'result_code': 0, 'result_msg': None}