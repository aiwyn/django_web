# -*- coding: utf-8 -*-
import math, datetime, pytz, random
from campaigns.foundation.applet import response, utils
from campaigns.foundation.const import FoundationConst, DisplayConst
from campaigns.yh import models, config, const, wechat_api
from campaigns.yh.applet import decorators
from campaigns.yh.applet.vote import FendaVoteManager
from campaigns.yh.applet.uitls import fit_up_work_list, save_work_image, fit_up_work
from campaigns.foundation.applet import cos
from django.utils import timezone
from collections import Counter
from campaigns.yh.applet.Tcos import Auth



@decorators.action_render
def upload(request):
    try:
        usrDream = request.POST['String'].encode("utf-8")
        usrImage = request.POST['Image'].encode("utf-8")
        usrName = request.POST['name'].encode("utf-8")
        # usrId = request.session.get("wxUser")
        usrId = "cain"
        usrId = models.WXUser.objects.filter(openid=usrId).first()
        authorUsr = models.Author.objects.create(wxUser=usrId)
        usrWork = models.Work.objects.create(
            type=0,
            name=usrName,
            string=usrDream,
            imageurl=usrImage,
            author=authorUsr,
            status=10,
        )
        return {"result_code": 0, "result_msg": "SUCCESS", "id": usrWork.id}
    except Exception as e:
        return {"result_code": 1, "result_msg": str(e)}


@decorators.action_render
def random_dream(request):
    try:
        l1 = []
        dreamId = models.Work.objects.all()
        for i in dreamId:
            l1.append(i.id)
        randomDream = l1[random.randint(0, len(l1) - 1)]
        workDream = models.Work.objects.get(id=randomDream)
        return {"name": workDream.name, "id": workDream.id, "String": workDream.string, "Image": str(workDream.imageurl), "vote": workDream.votedCount, "result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": -1, "result_msg": e}


@decorators.action_render
def fetch_dream(request):
    try:
        now_page = int(request.POST['nowPage'])
        page_rows = int(request.POST['pageRows'])
        total_count = models.Work.objects.filter(status=FoundationConst.STATUS_ONLINE).count()
        total_pages = int(math.ceil(float(total_count) / float(page_rows)))
        start = (now_page - 1) * page_rows
        end = start + page_rows
        workList = models.Work.objects.filter(status=FoundationConst.STATUS_ONLINE).all()[start: end]
        l1 = []
        for i in workList:
            d1 = {}
            d1['name'] = i.name
            d1['id'] = i.id
            d1['String'] = i.string
            d1['Image'] = str(i.imageurl)
            d1['vote'] = i.votedCount
            l1.append(d1)
        return {"worklist": l1, "total_pages": total_pages, "result_code": 0, "result_msg": None}
    except Exception as e:
        return {"result_code": 1, "result_msg": e}


@decorators.action_render
def dreamVote(request):
    try:
        voteId = request.POST['id']
        # usrInfo = request.session.get("wxUser")
        usrInfo = "cain"
        now = timezone.now()
        nowTime = datetime.datetime(now.year, now.month, now.day, tzinfo=pytz.utc)
        print nowTime
        voteDream = models.Vote.objects.filter(work_id=voteId).filter(creationTime=nowTime).first()
        print 111
        if voteDream is not None:
            return {"result_code": 1, "result_msg": "您今天已经投过票"}
        else:
            dreamWork = models.Work.objects.filter(id=voteId).first()
            wxUser = models.WXUser.objects.filter(openid=usrInfo).first()
            models.Vote.objects.create(
                work=dreamWork,
                wxUser=wxUser,
                status=10
            )
            nowVote = dreamWork.votedCount + 1
            dreamWork = models.Work.objects.filter(id=voteId).update(voteCount=nowVote)
            return {"result_code": 0, "result_msg": "SUCCESS"}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}


@decorators.action_render
def get_sign_package(request):
    try:
        url = request.POST['url']
    except Exception as e:
        raise utils.ClientException('{0}:{1}'.format(DisplayConst.EXCEPTION_CLIENT_INCOMPLETE_INFORMATION, str(e)))
    sign_package = wechat_api.WechatApi().get_sign_package(url)
    return sign_package


@decorators.action_render
def fetch_self(request):
    try:
        # wxUser = request.session.get("wxUser")
        wxUser = "cain"
        usrDream = models.Work.objects.filter(author__wxUser__openid=wxUser).first()
        if usrDream is not None:
            return {"String": usrDream.string, "name": usrDream.name, "image": str(usrDream.imageurl), "id": usrDream.id, "vote": usrDream.votedCount
                ,"result_code": 0, "result_msg": None}
        else:
            return {"result_code": 1, "result_msg": "未上传"}
    except Exception as e:
        return {"result_code": -1, "result_msg": e}


@decorators.action_render
def finish(request):
    try:
        name = request.POST['name']
        phone = request.POST['phone']
        # wxUser = request.session.get("wxUser")
        wxUser = "cain"
        usrDream = models.Author.objects.filter(wxUser__openid=wxUser).update(name=name, cellphone=phone)
        return {"result_code": 0, "result_msg": "success"}
    except Exception as e:
        return {"result_code": -1, "result_msg": e}


@decorators.action_render
def exportExcel(request):
    try:
        l2 = []
        l1 = []
        l3 = []
        pvData = models.PageView.objects.all().order_by("creationTime")             # 按照时间排序获得pv所有数据
        uvData = models.UniqueVisitor.objects.all().order_by("creationTime")        # 按照时间排序获得uv所有数据
        for u in uvData:
            l2.append(u.creationTime)
        for i in pvData:
            l1.append(i.creationTime)
        d1 = dict(Counter(l1))                                                     # counter计数模块返回列表中同元素出现次数
        d2 = dict(Counter(l2))
        for i, j, d in d1.keys(), d1.values(), d2.values():
            d3 = {}
            d3['date'] = i,
            d3['pv'] = j
            d3['uv'] = d
            l3.append(d3)
        exPorter = decorators.exportExcel(request=request, name="每日PUV", dict1=l3)
        return exPorter
    except Exception as e:
        return {"result_code": 1, "result_msg": None}


@decorators.action_render
def tocloud(request):
    try:
        sign_type = request.GET.get("sign_type", None)
        if sign_type == "appSign":
            expired = request.GET.get("expired", None)
            bucketName = request.GET.get("bucketName", None)
            if expired is None or bucketName is None:
                return {"code": 10001, "message": "缺少expired或bucketName"}
            else:
                sign = Auth()
                sign = sign.appSign(expired=expired, bucketName=bucketName)
                return {"code": 0, "message": "成功", "data": sign}

        elif sign_type == "appSign_once":
            path = request.GET.get("path", None)
            bucketName = request.GET.get("bucketName", None)
            if path or bucketName is None:
                return {"code": 10001,"message": "缺少path或bucketName"}
            else:
                sign = Auth()
                sign = sign.appSign_once(path, bucketName)
                return {"code": 0, "message": "成功", "data": sign}

        else:
            return {"code": 10001, "message": "未指定签名方式"}
    except Exception as e:
        return {"code": -1, "message": "内部错误reason：" + str(e)}
