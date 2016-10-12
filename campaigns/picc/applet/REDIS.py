from django.conf import settings
from django.core.cache import cache
import json

class djangoCache(object):

    def __init__(self, key):
        self.key = key

    def loadData(self):
        key = self.key
        value = cache.get(key)
        if value == None:
            data = None
        else:
            data = value
        return data

    def saveData(self, value, save_type):
            key = self.key
            try:
                if save_type == 1:
                   cache.set(key, value, settings.REDIS_TIMEOUT)
                elif save_type == 2:
                    cache.set(key, value, settings.CUBES_REDIS_TIMEOUT)
                elif save_type == 3:
                    cache.set(key, value, settings.ACCESS_TIMEOUT)
                else:
                    cache.set(key, value, settings.NEVER_REDIS_TIMEOUT)
                return "SUCCESS"
            except Exception as e:
                return str(e)