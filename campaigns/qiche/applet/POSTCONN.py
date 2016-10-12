#coding=utf-8
import json, suds
def Webservice(DATA):
    _data = json.dumps(DATA)
    client = suds.client.Client("http://ddmp.audi-online.cn:86/BaseInfoService.svc?wsdl")
    result = client.service.SendLeads(_data)
    return result
