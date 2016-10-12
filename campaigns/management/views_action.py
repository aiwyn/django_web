# -*- coding: utf-8 -*-
import time
from campaigns.management.applet import decorators, utils
from campaigns.foundation.const import DisplayConst
from campaigns.management import models, const
from django.http import HttpResponse


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



