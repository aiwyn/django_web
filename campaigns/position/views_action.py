from campaigns.position import models
from campaigns.position.applet import decorators
from django.http import HttpResponse

def regiter(request):
    name = request.POST['name']
    passwd = request.POST['passwd']
    userlvl = request.POST['lvl']
    try:
        userinfo = models.adminuser.objects.create(
            lvl=userlvl,
            name=name,
            passwd=passwd,
        )
        return {"result_code": 0, "result_msg": "success"}
    except Exception as e:
        return {"result_code": 1, "result_ msg": str(e)}


def login(request):
    name = request.POST['name']
    passwd = request.POST['passwd']
    try:
        userinfo = models.adminuser.objects.filter(name=name, passwd=passwd).first()
        if userinfo is not None:
            return {"result_code": 0, "result_msg": "welcome back" + str(name)}
        else:
            return {"result_code": 1, 'result_msg': "user info error!"}
    except Exception as e:
        return {"result_code": -1, "result_msg": str(e)}



def addinfo(request):
    lat = request.POST['lat']
    long = request.POST['long']
    name = request.POST['name']
    try:
        positioninfo = models.positinfo.objects.create(
            name=name,
            lat=lat,
            long=long,
        )
        return {"result_code": 0, "result_msg": "add position success"}
    except Exception as e:
        return {"result_code": 1, "result_msg": str(e)}