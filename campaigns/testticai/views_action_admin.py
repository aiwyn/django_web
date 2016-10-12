# -*- coding: utf-8 -*-
# 后台控制接口
import time, datetime, pytz, config
import random, json
from django.utils import timezone
from campaigns.foundation.const import FoundationConst
from campaigns.testticai import models, const
from campaigns.testticai.applet.uitls import save_work_file
from campaigns.testticai.applet import decorators, QRCode


# 奖卷信息查询
@decorators.action_render
def priceInfo(request):
    try:
        nowpage = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (nowpage - 1) * page_rows
        end = start + page_rows
        startime = timezone.datetime.strptime(request.GET['startime'], "%Y-%m-%d").date()
        endtime = timezone.datetime.strptime(request.GET['endtime'], "%Y-%m-%d").date()
        total_count = models.walkCount.objects.filter(priCode__isnull=False).filter(creaTime__lte=endtime).filter(creaTime__gte=startime).all().count()
        hitPrizeinfo = models.walkCount.objects.filter(priCode__isnull=False).filter(creaTime__lte=endtime).filter(creaTime__gte=startime).all()
        l1 = []
        for i in hitPrizeinfo:
            d1 = {}
            wxObj = models.WXUser.objects.filter(openid=i.openid).first()
            d1['id'] = wxObj.id
            inFo = models.qrcount.objects.filter(id=int(i.priCode))[0]
            d1['pricode'] = str(inFo.code)
            d1['endtime'] = inFo.endtime
            d1['sendTime'] = inFo.sendTime
            l1.append(d1)
        if request.GET['excel'] == '1':
            excel = decorators.exportExcel(request, name='pricode', dict1=l1)
            return excel
        else:
            return {"list": l1, "total_count": total_count, "result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": 1, "result_msg": e}


# 查看中奖用户
@decorators.action_render
def fetchPriz(request):
    try:
        Type = request.GET['type']
        nowpage = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (nowpage - 1) * page_rows
        end = start + page_rows
        if Type == "week":
            inFo = models.hitprize.objects.filter(isSend=1, countType=0).all()
            if inFo is not None:
                for d in inFo:
                    walkList = json.loads(d.usrList)['data']
                    l1 = []
                    for i in walkList:
                        d1 = {}
                        openID = models.WXUser.objects.filter(openid=i["user"]).first()
                        d1['id'] = openID.id
                        d1['walk'] = i['walk']
                        d1['weekCount'] = d.weekMacht
                        l1.append(d1)
                    if request.GET['excel'] == 1:
                        excel = decorators.exportExcel(request, name='pricode', dict1=l1)
                        return excel
                    else:
                        return {"countList": l1[start: end], "result_code": 0, "result_msg": None, "total_count": len(l1)}
            else:
                return {"result_code": 2, "result_msg": "暂无数据"}
        if Type == "day":
            inFo = models.hitprize.objects.filter(isSend=1, countType=1).all()
            if inFo is not None:
                for d in inFo:
                    walkList = json.loads(d.usrList)['data']
                    l1 = []
                    for i in walkList:
                        d1 = {}
                        d1['id'] = models.WXUser.objects.get(openid=models.walkCount.objects.get(id=i["user"]).openid).id
                        d1['walk'] = i['walk']
                        d1['weekCount'] = d.weekMacht
                        l1.append(d1)
                    if request.GET['excel'] == 1:
                        excel = decorators.exportExcel(request, name='pricode', dict1=l1)
                        return excel
                    else:
                        return {"countList": l1[start: end],"total_count": len(l1), "result_code": 0, "result_msg": None}
                else:
                    return {"result_code": 2, "result_msg": "暂无数据"}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}



# 上传奖券文件
@decorators.action_render
def upload(request):
    try:
        filename = save_work_file((request.FILES[const.ViewConst.RN_WORK_IMAGE]))
        file = codefile = models.addCode.objects.create(
            File=filename
        )
        return {'result_code': 0, "result_msg": None, 'id': file.id}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}


# 生成奖券以及二维码
@decorators.action_render
def startAdd(request):
    try:
        addID = request.GET['id']
        fileName = models.addCode.objects.filter(id=addID).filter(issuccess=1).first()
        if fileName is not None:
            fileUrl = str(fileName.File).strip("./")
            start_add = QRCode.addQRCODE(fileUrl)
            runDraw = start_add.startDraw()
            if runDraw == "success":
                models.addCode.objects.filter(id=addID).update(issuccess=0)
                return {"result_code": 0, "result_msg": 'success'}
            else:
                return {"result_code": -1, "result_msg": runDraw}
        else:
            return {"result_code": 1, "result_msg": "重复操作"}
    except Exception as e:
        return {"result_code": -2, "result_msg": e}


# 查询当前奖品池
@decorators.action_render
def fetchCode(request):
    try:
        nowpage = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (nowpage - 1) * page_rows
        end = start + page_rows
        l1 = []
        total_count = models.qrcount.objects.all().count()
        for i in models.qrcount.objects.all()[start: end]:
            d1 = {}
            d1["code"] = i.code
            d1['passwd'] = i.passwd
            d1['img'] = str(i.qrimg)
            d1['startime'] = i.startime
            d1['endtime'] = i.endtime
            d1['isend'] = i.isend
            d1['sendTime'] = i.sendTime
            l1.append(d1)
        return {"code_list": l1, "total_count": total_count, "result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}


# pv uv
@decorators.action_render
def _PUv(request):
    try:
        Pcount = models.CountPUV.objects.filter(id=1)[0]
        _PV = int(Pcount.pv) + int(Pcount.addpv)
        _UV = int(Pcount.uv) + int(Pcount.adduv)
        return {"pv": _PV, "uv": _UV, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {"pv": None, "uv": None, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: e}



# 管理员登录
@decorators.action_render
def AdminLogIn(request):
    username = request.POST['username']
    passwd = request.POST['passwd']
    usrinfo = models.AdminUser.objects.filter(username=username).first()
    if usrinfo is not None:
        if passwd == usrinfo.userpasswd:
            request.session['usrname'] = username
            return {FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: "登陆成功"}
        else:
            return {FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: "密码错误"}
    else:
        return {FoundationConst.RN_RCODE: 2, FoundationConst.RN_RMSG: "用户名错误"}





# 活动数据
@decorators.action_render
def ActiveData(request):
    try:
        nowpage = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (nowpage - 1) * page_rows
        end = start + page_rows
        total_count = models.walkCount.objects.all().count()
        if request.GET['type'] == "1":
            activedata = models.walkCount.objects.all()
            l1 = []
            for i in activedata:
                d2 = {}
                d2['id'] = i.info.id
                d2['cid'] = i.id
                d2['picture'] = str(i.image)
                d2['count'] = i.walk
                d2['change'] = i.change
                d2['money'] = i.money
                d2['pricesname'] = i.priCode
                d2['update'] = str(i.creaTime)
                d2['phonecall'] = i.info.usractive
                l1.append(d2)
            excel = decorators.exportExcel(request, name="活动数据", dict1=l1)
            return excel
        elif request.GET['suchchoice'] == "time":
            activedata = models.walkCount.objects.all().order_by("-creaTime")[start: end]
            l1 = []
            for i in activedata:
                if i.image is None:
                    continue
                else:
                    d1 = {}
                    d1['id'] = i.info.id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['update'] = str(i.creaTime)
                    d1['phonecall'] = i.info.usractive
                    l1.append(d1)
            return {"acivedata": l1, "total_count": total_count, FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: None}
        else:
            activedata = models.walkCount.objects.all().order_by("-walk")[start: end]
            l1 = []
            for i in activedata:
                d1 = {}
                d1['id'] = i.info.id
                d1['Cid'] = i.id
                d1['picture'] = str(i.image)
                d1['count'] = i.walk
                d1['change'] = i.change
                d1['money'] = i.money
                d1['pricesname'] = i.priCode
                d1['update'] = str(i.creaTime)
                d1['phonecall'] = i.info.usractive
                l1.append(d1)
            return {"acivedata": l1, "total_count": total_count, FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {"activedata": None, "total_count": None, FoundationConst.RN_RCODE: -1, FoundationConst.RN_RMSG: e}




# 用户数据
@decorators.action_render
def UserData(request):
    try:
        now_page = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        USRDATA = models.WXUser.objects.all()
        start = (now_page - 1) * page_rows
        end = start + page_rows
        l1 = []
        for i in USRDATA:
            userdata = models.walkCount.objects.filter(openid=i.openid).all()
            usercount = len(userdata.values_list())
            if userdata is not None:
                count = 0
                Pcount = 0
                a = None
                for _i in userdata:
                    if int(_i.change) <= 0:
                        count += int(_i.walk)
                    else:
                        count += int(_i.change)
                    a = _i.info.id
                d1 = {}
                d1['money'] = round(float(count) / 2000, 2) + Pcount
                d1['username'] = a
                d1['count'] = count
                d1['joincount'] = usercount
                l1.append(d1)
            else:
                continue
        if request.GET['suchchoice'] == "time":
            l2 = sorted(l1, key=lambda x: x["joincount"], reverse=True)
            total_page = len(l2)
        else:
            l2 = sorted(l1, key=lambda x: x["count"], reverse=True)
            total_page = len(l2)
        return {"userdata": l2[start: end], 'total_page': total_page, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {"userdata": None, FoundationConst.RN_RCODE: -1, 'total_page': None, FoundationConst.RN_RMSG: str(e)}


# 实物奖品
@decorators.action_render
def SWPrices(request):
    try:
        Getype = request.GET['type']
        now_page = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (now_page - 1) * page_rows
        end = start + page_rows
        swcount = models.walkCount.objects.filter(priCode__isnull=False).all().count()
        if Getype == "1":
            SWPrice = models.walkCount.objects.filter(priCode__isnull=False).all()

            l1 = []
            for i in SWPrice:
                d1 = {}
                d1['userid'] = i.usrinfo_id
                d1['pricesname'] = i.priCode
                d1['updatetime'] = str(i.creaTime)
                d1['phonecall'] = i.info.usrprizes
                l1.append(d1)
            excel = decorators.exportExcel(request, '实物奖品', l1)
            return excel
        else:
            SWPrice = models.walkCount.objects.filter(priCode__isnull=False).all()[start: end]

            l1 = []
            for i in SWPrice:
                d1 = {}
                d1['userid'] = i.info_id
                d1['pricesname'] = i.priCode
                d1['updatetime'] = str(i.creaTime)
                d1['phonecall'] = i.info.usrprizes
                l1.append(d1)
            return {'swdata': l1, 'total_page': swcount, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {'swdata': None, FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: str(e)}


# 线下报名
@decorators.action_render
def SignUp(request):
    try:
        now_page = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (now_page - 1) * page_rows
        end = start + page_rows
        total_count = models.UsrPhoneCall.objects.all().count()
        offlinesign = models.UsrPhoneCall.objects.all()[start: end]
        l1 = []
        d1 = {}
        for i in offlinesign:
            d1['userid'] = i.id
            _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.signuptime))
            d1['updatetime'] = _time
            d1['phonecall'] = i.usrsignup
            l1.append(d1)
        Getype = request.GET['type']
        if Getype == "1":
            offlinesign = models.UsrPhoneCall.objects.all()
            l1 = []
            d1 = {}
            for i in offlinesign:
                d1['userid'] = i.id
                _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.signuptime))
                d1['updatetime'] = _time
                d1['phonecall'] = i.usrsignup
                l1.append(d1)
            excel = decorators.exportExcel(request, '线下报名', l1)
            return excel
        else:
            return {"signup": l1, 'total_count': total_count, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {'signup': None, 'total_count': None, FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: str(e)}


# 活动数据搜寻
@decorators.action_render
def SuchActive(request):
    try:
        now_page = int(request.POST['now_page'])
        page_rows = int(request.POST['page_rows'])
        start = (now_page - 1) * page_rows
        end = start + page_rows
        usrid = request.POST.get("id", False)
        if usrid != "None":
            l1 = []
            timestart = request.POST['timestart']
            timend = request.POST['timend']
            total_count = models.walkCount.objects.filter(info__id=usrid, updatetime__gte=timestart,
                                                           updatetime__lte=timend).all().count()

            if request.POST['type'] == "time" and request.POST['extype'] == "0":
                userinfo = models.walkCount.objects.filter(usrinfo__id=usrid, updatetime__gte=timestart,
                                                            updatetime__lte=timend).all().order_by('-updatetime')[start: end]
                for i in userinfo:
                    d1 = {}
                    d1['usrid'] = i.info_id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['updatetime'] = str(i.creaTime)
                    d1['username'] = i.info.usractive
                    l1.append(d1)
                return {"suchdata": l1, 'total_count': total_count, FoundationConst.RN_RCODE: 0,
                        FoundationConst.RN_RMSG: None}
            elif request.POST['extype'] == "1":
                userinfo = models.walkCount.objects.filter(info__id=usrid, updatetime__gte=timestart,
                                                            updatetime__lte=timend).all()
                for i in userinfo:
                    d1 = {}
                    d1['usrid'] = i.info_id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['updatetime'] = str(i.creaTime)
                    d1['username'] = i.info.usractive
                    l1.append(d1)
                excel = decorators.exportExcel(request, name='活动数据', dict1=l1)
                return excel
            else:
                userinfo = models.walkCount.objects.filter(info__id=usrid, updatetime__gte=timestart,
                                                            updatetime__lte=timend).all().order_by('-count')[start: end]
                for i in userinfo:
                    d1 = {}
                    d1['usrid'] = i.info_id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['updatetime'] = str(i.creaTime)
                    d1['username'] = i.info.usractive
                    l1.append(d1)
                return {"suchdata": l1, 'total_count': total_count, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
        else:
            l1 = []
            timestart = request.POST['timestart']
            timend = request.POST['timend']
            total_count = models.walkCount.objects.filter(updatetime__gte=timestart,
                                                           updatetime__lte=timend).all().count()

            if request.POST['type'] == 'time' and request.POST['extype'] == None:
                userinfo = models.walkCount.objects.filter(updatetime__gte=timestart,
                                                            updatetime__lte=timend).all().order_by(
                    '-updatetime')[start: end]
                for i in userinfo:
                    d1 = {}
                    d1['usrid'] = i.info_id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['updatetime'] = str(i.creaTime)
                    d1['username'] = i.info.usractive
                    l1.append(d1)
                return {"suchdata": l1, 'total_count': total_count, FoundationConst.RN_RCODE: 0,
                        FoundationConst.RN_RMSG: None}
            elif request.POST['extype'] == "1":
                userinfo = models.walkCount.objects.filter(updatetime__gte=timestart,
                                                            updatetime__lte=timend).all()
                for i in userinfo:
                    d1 = {}
                    d1['usrid'] = i.info_id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['updatetime'] = str(i.creaTime)
                    d1['username'] = i.info.usractive
                    l1.append(d1)
                excel = decorators.exportExcel(request, name='活动数据', dict1=l1)
                return excel
            else:
                userinfo = models.walkCount.objects.filter(updatetime__gte=timestart,
                                                            updatetime__lte=timend).all().order_by(
                    '-count')[start: end]
                for i in userinfo:
                    d1 = {}
                    d1['usrid'] = i.info_id
                    d1['Cid'] = i.id
                    d1['picture'] = str(i.image)
                    d1['count'] = i.walk
                    d1['change'] = i.change
                    d1['money'] = i.money
                    d1['pricesname'] = i.priCode
                    d1['updatetime'] = str(i.creaTime)
                    d1['username'] = i.info.usractive
                    l1.append(d1)
                    l1.append(d1)
                return {"suchdata": l1, 'total_count': total_count, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {FoundationConst.RN_RCODE: -1, FoundationConst.RN_RMSG: e}



# 用户数据搜寻
@decorators.action_render
def SuchUser(request):
    try:
        now_page = int(request.POST['now_page'])
        page_rows = int(request.POST['page_rows'])
        start = (now_page - 1) * page_rows
        end = start + page_rows
        usrid = request.POST['id']
        d1 = {}
        l1 = []
        total_count = models.walkCount.objects.filter(info__id=usrid).all().count()
        if request.POST['suchchoice'] == "time":
            userdata = models.walkCount.objects.filter(info__id=usrid).all().order_by('-updatetime')[start: end]
        else:
            userdata = models.walkCount.objects.filter(info__id=usrid).all().order_by('-count')[start: end]
        usercount = len(userdata.values_list())
        if userdata is not None:
            count = 0
            Pcount = 0
            a = None
            for _i in userdata:
                if _i.change is None:
                    count += int(_i.walk)
                else:
                    count += int(_i.walk)
                a = _i.info.id
            d1['money'] = round(float(count) / 2000, 2) + Pcount
            d1['username'] = a
            d1['count'] = count
            d1['joincount'] = usercount
            l1.append(d1)
        return {"userdata": l1, 'total_count': total_count, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {"userdata": None, 'total_count': None, FoundationConst.RN_RCODE: -1, FoundationConst.RN_RMSG: str(e)}


# 线下报名搜寻
@decorators.action_render
def SuchSign(request):
    try:
        now_page = int(request.POST['now_page'])
        page_rows = int(request.POST['page_rows'])
        start = (now_page - 1) * page_rows
        end = start + page_rows
        usrid = request.POST['id']
        if usrid is not None:
            timestart = request.POST['timestart']
            timend = request.POST['timend']
            timestart = time.mktime(time.strptime(timestart, '%Y-%m-%d'))
            timend = time.mktime(time.strptime(timend, '%Y-%m-%d'))
            offlinesign = models.UsrPhoneCall.objects.filter(id=usrid, signuptime__gte=float(timestart), signuptime__lte=float(timend)).all()
            totalcount = offlinesign.count()
            Getype = request.POST['type']
            if Getype == "1":
                l1 = []
                for i in offlinesign:
                    d1 = {}
                    d1['userid'] = i.id
                    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.signuptime))
                    d1['updatetime'] = _time
                    d1['phonecall'] = i.usrsignup
                    l1.append(d1)
                excel = decorators.exportExcel(request, '线下报名', l1)
                return excel
            else:
                offlinesign = offlinesign[start: end]
                l1 = []

                for i in offlinesign:
                    d1 = {}
                    d1['userid'] = i.id
                    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.signuptime))
                    d1['updatetime'] = _time
                    d1['phonecall'] = i.usrsignup
                    l1.append(d1)
                return {"signup": l1, 'total_count': totalcount, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
        else:
            timestart = request.POST['timestart']
            timend = request.POST['timend']
            timestart = float(time.mktime(time.strptime(timestart, '%Y-%m-%d')))
            timend = float(time.mktime(time.strptime(timend, '%Y-%m-%d')))
            offlinesign = models.UsrPhoneCall.objects.filter(signuptime__gte=timestart, signuptime__lte=timend).all()
            totalcount = offlinesign.count()
            Getype = request.POST['type']
            if Getype == "1":
                l1 = []
                for i in offlinesign:
                    d1 = {}
                    d1['userid'] = i.id
                    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.signuptime))
                    d1['updatetime'] = _time
                    d1['phonecall'] = i.usrsignup
                    l1.append(d1)
                excel = decorators.exportExcel(request, '线下报名', l1)
                return excel
            else:
                offlinesign = offlinesign[start: end]
                l1 = []
                for i in offlinesign:
                    d1 = {}
                    d1['userid'] = i.id
                    _time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.signuptime))
                    d1['updatetime'] = _time
                    d1['phonecall'] = i.usrsignup
                    l1.append(d1)
                return {"signup": l1, 'total_count': totalcount, FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: None}
    except Exception as e:
        return {'signup': None, FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: str(e)}


@decorators.action_render
def ChangeCount(request):
    try:
        Cid = request.POST['Cid']
        CC = request.POST['change']
        money = round(float(CC) / 2000, 2)
        Info = models.walkCount.objects.filter(id=Cid)
        adminame = request.session.get('usrname')
        things = "管理员： " + str(adminame) + "修改用户步数为： " + str(CC) + "金钱变更为: " + str(money) + "原步数为: " + str(Info[0].walk)
        activelog = models.AdminLog.objects.create(usrname=adminame, event=things)
        Info.update(money=str(money), change=CC)
        return {FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: "success"}
    except Exception as e:
        return {FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: str(e)}


# 改变pv uv
@decorators.action_render
def ChangePUv(request):
    try:
        addpv = request.POST['pv']
        adduv = request.POST['uv']
        PUv = models.CountPUV.objects.filter(id=1)
        adminame = request.session.get('usrname')
        THINGS = "管理员: " + adminame + "增加FAKE PV UV 为： " + addpv + " " + adduv + "原FAKE PV UV 数据为： " + PUv[0].addpv + " " + PUv[0].adduv
        PUv.update(addpv=addpv, adduv=adduv)
        models.AdminLog.objects.create(name=adminame, event=THINGS)
        return {FoundationConst.RN_RCODE: 0, FoundationConst.RN_RMSG: "success"}
    except Exception as e:
        return {FoundationConst.RN_RCODE: 1, FoundationConst.RN_RMSG: str(e)}

#
# @decorators.action_render
# def hitPrize(request):
#     try:
#         watchType = request.GET['type']
#         now = timezone.now()
#         dateTime = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=pytz.utc)
#         if watchType == "week":
#             hitprize = models.hitprize.objects.filter(creatime__gte=dateTime).filter(isSend=1).filter(countType=0).first()
#         elif watchType == "day":
#             hitprize = models.hitprize.objects.filter(creatime__gte=dateTime).filter(isSend=1).filter(
#                 countType=1).first()
#         else:
#             hitprize = models.hitprize.objects.filter(creatime__gte=dateTime).filter(isSend=1).filter(
#                 countType=3).first()
#         if hitprize is None:
#             return {"result_code": 1, "result_msg": None}
#         else:
#             prizeList = json.loads(hitprize.usrList)
#             return {"prizeList": prizeList, "result_code": 0, "result_msg": None, "id": hitprize.id}
#     except Exception as e:
#         return {"result_code": -1, "result_msg": e}

@decorators.action_render
def fetchDay(request):
    try:
        startime = request.GET['startime']
        endtime = request.GET['endtime']
        now_page = int(request.GET['now_page'])
        page_rows = int(request.GET['page_rows'])
        start = (now_page - 1) * page_rows
        end = start + page_rows
        endtime = str(endtime.split("-")[0]) + "-" + str(endtime.split("-")[1]) + "-" + str(int(endtime.split("-")[2]) + 1)
        valueList = models.hitprize.objects.filter(creatime__gte=startime).filter(creatime__lte=endtime).all()
        total_count = valueList.count()
        l1 = []
        for i in valueList[start: end]:
            d1 = {}
            d1['id'] = i.id
            d1['countType'] = i.countType
            d1['isSend'] = i.isSend
            d1['week'] = i.weekMacht
            d1['creatime'] = str(i.creatime)
            l1.append(d1)
        return {"priceList": l1, "result_code": 1, "result_msg": None, 'total_count': total_count}
    except Exception as e:
        return {"result_code": -1, "result_msg": e}


@decorators.action_render
def fetchCount(request):
    try:
        now_page = int(request.POST['now_page'])
        page_rows = int(request.POST['page_rows'])
        id = request.POST['id']
        start = (now_page - 1) * page_rows
        end = start + page_rows
        valueList = models.hitprize.objects.filter(id=id).first()
        countList = json.loads(valueList.usrList)['data']
        return {"priceList": countList[start: end], "total_count": len(countList), "result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}


# 发日奖
@decorators.action_render
def sendPrize(request):
    try:
        iD = request.POST['id']
        PRICESINFO = models.hitprize.objects.filter(id=iD).filter(countType=1).first()
        if PRICESINFO is None:
            return {"result_code": 0, "result_msg": "error!!"}
        else:
            weekCount = PRICESINFO.weekMacht
            now = timezone.datetime.now()
            priceCount = models.qrcount.objects.filter(isend=1).all()
            if weekCount == 1:
                startTime = datetime.datetime.utcfromtimestamp(config.WorkConfig.starTime)
                startTime = datetime.datetime(startTime.year, startTime.month, startTime.day, 0, 0, 0, tzinfo=pytz.utc)
            elif weekCount == 2:
                startTime = datetime.datetime.utcfromtimestamp(config.WorkConfig.starTime)
                startTime = datetime.datetime(startTime.year, startTime.month, startTime.day, 0, 0, 0, tzinfo=pytz.utc) + datetime.timedelta(days=7)
            else:
                startTime = datetime.datetime.utcfromtimestamp(config.WorkConfig.starTime)
                startTime = datetime.datetime(startTime.year, startTime.month, startTime.day, 0, 0, 0,
                                              tzinfo=pytz.utc) + datetime.timedelta(days=14)
            priceList = json.loads(PRICESINFO.usrList)['data']
            isUseList = models.walkCount.objects.filter(creaTime__gte=startTime).filter(priCode__isnull=False).all()
            l1 = []
            for j in isUseList:
                l1.append(j.id)
            for i in priceList:
                if i['user'] in l1:
                    priceList.remove(i)
            if len(priceList) < 3000:

                for i, j in zip(priceList, priceCount):
                    models.walkCount.objects.filter(id=i['id']).update(priCode=j.id)
                    models.qrcount.objects.filter(id=j.id).update(isend=0, sendTime=now)
            else:
                for i, j in zip(priceList[0: 2999], priceCount):
                    models.walkCount.objects.filter(id=i['id']).update(priCode=j.id)
                    models.qrcount.objects.filter(id=j.id).update(isend=0, sendTime=now)
            models.hitprize.objects.filter(id=iD).filter(countType=1).update(isSend=0)
            return {"result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": 1, "result_msg": e}


# 生成总排名
@decorators.action_render
def allCount(request):
    try:
        nowDay = datetime.date.today()
        matchWeek = datetime.date.fromtimestamp(config.WorkConfig.starTime)
        priceInfo = models.hitprize.objects.filter(countType=2)
        l1 = []
        wxUser = models.WXUser.objects.all()
        for d in wxUser:
            d1 = {}
            d1['user'] = d.id
            count = 0
            walkInfo = models.walkCount.objects.filter(creaTime__gte=matchWeek).filter(creaTime__lte=nowDay).filter(openid=d.openid).all()
            for i in walkInfo:
                if int(i.change) != 0:
                    count += int(i.change)
                else:
                    count += int(i.walk)
            d1['walk'] = count
            l1.append(d1)
        d1 = {}
        d1['data'] = l1
        if priceInfo[0] is None:
            models.hitsprize.objects.create(
                countType=2,
                usrList=json.dumps(d1),
                weekMacht=3
            )
        else:
            priceInfo.update(usrList=json.dumps(d1))

        return {"result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e  )}


# 生成周排名
@decorators.action_render
def makeWeek(request):
    try:
        nowDay = datetime.date.today()
        matchWek = int(str(nowDay - datetime.date.fromtimestamp(config.WorkConfig.starTime)).split(" ")[0])
        if 0 < matchWek <= 7:
            weekCount = 1

        elif 7 < matchWek <= 14:
            weekCount = 2
            matchWek -= 7
        else:
            weekCount = 3
            matchWek -= 14
        startday = nowDay - datetime.timedelta(days=matchWek)
        firstWeek = models.hitprize.objects.filter(weekMacht=weekCount).filter(countType=0).filter(isSend=1)
        l1 = []
        wxUser = models.WXUser.objects.all()
        for d in wxUser:
            d1 = {}
            d1['user'] = d.id
            count = 0
            walkInfo = models.walkCount.objects.filter(creaTime__gte=startday).filter(creaTime__lte=nowDay).filter(openid=d.openid).all().order_by('creaTime')
            for i in walkInfo:
                if int(i.change) != 0:
                    count += int(i.change)
                else:
                    count += int(i.walk)
            d1['walk'] = count
            l1.append(d1)
        if firstWeek.first() is not None:
            d1 = {}
            l1 = sorted(l1, key=lambda x: x["walk"], reverse=True)
            count = 1
            for i in l1:
                i["rank"] = count
                count += 1
            d1['data'] = l1
            firstWeek.update(usrList=json.dumps(d1), creatime=timezone.datetime.now())
            return {"result_code": 0, "result_msg": "数据已更新"}
        else:
            d1 = {}
            l1 = sorted(l1, key=lambda x: x["walk"], reverse=True)
            count = 1
            for i in l1:
                i["rank"] = count
                count += 1
            d1['data'] = l1
            models.hitprize.objects.create(
                usrList=json.dumps(d1),
                countType=0,
                weekMacht=weekCount,
                creatime=timezone.datetime.now()
            )
            return {"result_code": 0, "result_msg": "数据已创建"}
    except Exception as e:
        return {"result_code": -1, "result_msg": e}


# 生成日排行
@decorators.action_render
def dayCount(request):
    nowday = datetime.date.today()
    weekDayd = nowday - datetime.timedelta(days=1)
    matchWek = int(str(nowday - datetime.date.fromtimestamp(config.WorkConfig.starTime)).split(" ")[0])
    if 0 < matchWek <= 7:
        weekCount = 1
    elif 7 < matchWek <= 14:
        weekCount = 2
    else:
        weekCount = 3
    dataInfo = models.walkCount.objects.filter(creaTime__gte=weekDayd).filter(creaTime__lte=nowday).all().order_by('creaTime')
    dataInfo = sorted(dataInfo, key=lambda x: int(x.walk), reverse=True)
    rank = 1
    l1 = []
    for i in dataInfo:
        d1 = {}
        count = 0
        d1['id'] = i.id
        d1['rank'] = rank
        d1['walk'] = i.walk
        d1['user'] = models.WXUser.objects.filter(openid=i.openid).first().id
        d1['creatime'] = str(i.creaTime).split(" ")[0] + " " + str(i.creaTime).split(" ")[1].split(".")[0]
        rank += 1
        l1.append(d1)
    now = timezone.datetime.now()
    nowday = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
    isAdd = models.hitprize.objects.filter(creatime__gte=nowday).filter(countType=1).first()
    if isAdd is None:
        d1 = {}
        d1['data'] = l1
        models.hitprize.objects.create(
            usrList=json.dumps(d1),
            countType=1,
            weekMacht=weekCount,
        )
        return {"result_code": 0, "result_msg": "数据已创建"}
    else:
        if isAdd.isSend == 1:
            d1 = {}
            d1['data'] = l1
            models.hitprize.objects.filter(creatime__gte=nowday).filter(isSend=1).filter(countType=1).update(
                usrList=json.dumps(d1),
                countType=1,
                weekMacht=weekCount,
            )
            return {"result_code": 1,
                    "result_msg": "数据已更新"}
        else:
            return {"result_code": 2, "result_msg": "无法新建今日已发送"}


# 确认周排名
@decorators.action_render
def accessWeek(request):
    try:
        _id = request.POST['id']
        models.hitprize.objects.filter(id=_id).update(isSend=0)
        return {"result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": -1, "result_msg": e}