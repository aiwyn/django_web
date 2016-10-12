import urllib2, hashlib, hmac
def getSig(cfg):
    strFilter = ".-_"
    codeUrlAddr = urllib2.quote(cfg['urlAddr'],strFilter)
    urlData2 = sorted(cfg['urlData'].iteritems(), key=lambda d:d[0])
    codeStr0 = ""
    for (value01,value02) in urlData2:
        if codeStr0:
            codeStr0 += "&" + str(value01) + '=' + str(value02)
        else:
            codeStr0 += str(value01) + '=' + str(value02)
            codeStr1 = urllib2.quote(codeStr0)
            codeConn = cfg['urlMethod'] + '&' + codeUrlAddr + '&' + codeStr1
            sig = hmac.new(cfg['appkey'] + '&', codeConn, hashlib.sha1).digest().encode('base64').rstrip()
            return sig
def test():
    urlData = {		'openid' : '12345',		'openkey' : '12345',		'pf' : 'wanba_ts',		'appid' : 12345,		'format' : 'json',		'user_attr' : '{"level":%d}' % 1234	}
    urlcfg = {		'urlAddr' : '/v3/user/set_achievement',		'urlMethod' : 'GET',		'appkey' : 'ABCDWFSFFG',		'urlData' : urlData	}
    urlData['sig'] = getSig(urlcfg)