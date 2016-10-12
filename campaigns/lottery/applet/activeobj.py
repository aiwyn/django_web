from campaigns.foundation.const import FoundationConst
from campaigns.lottery import models
import time


class ActiveobjAdmin(object):
    def __init__(self, addactive):
        self.addactives = addactive
        # starttime = str(addactive.starttime.split("/")[0]) + "-" + str(addactive.starttime.split("/")[1]) + "-" + str(addactive.starttime.split("/")[2])
        # stoptime = str(addactive.stoptime.split("/")[0]) + "-" + str(addactive.stoptime.split("/")[1]) + "-" + str(addactive.stoptime.split("/")[2])
        starttime = str(addactive.starttime)
        stoptime = str(addactive.stoptime)
        __Activedays = int(time.mktime(time.strptime(stoptime, "%Y-%m-%d"))) - int(time.mktime(time.strptime(starttime, "%Y-%m-%d")))
        addactive.activedays = __Activedays / 3600 / 24
        models.activetime.objects.create(
            activename=addactive.activename,
            chance=addactive.chance,
            starttime=starttime,
            stoptime=stoptime,
            activedays=addactive.activedays,
            ucount=addactive.ucount,
            dcount=addactive.dcount
        )


class PrizesobjAdmin(object):
    def __init__(self, addprizes):
        self.addprizes = addprizes
        _prizes = models.activeinfo.objects.create(
            activeId=addprizes.activeId,
            prizeslvl=addprizes.prizeslvl,
            prizesname=addprizes.prizesname,
            quantity=addprizes.quantity,
            releasedate=addprizes.releasedate,
        )


        count = 1
        while True:
            if count > int(_prizes.quantity):
                break
            else:
                __prizes = models.Lottery_prizes.objects.create(
                    prizeslvl=_prizes.prizeslvl,
                    isdole=1,
                    userid=None,
                    activeid=_prizes.activeId,
                    prizesname=_prizes.prizesname,
                    activetime=int(time.mktime(time.strptime(str(_prizes.releasedate), "%Y-%m-%d")))
                )
                count = count + 1


class testdelete(object):
    def __init__(self, deleteprizes):
        print "success"