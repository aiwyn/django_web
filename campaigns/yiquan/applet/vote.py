# -*- coding: utf-8 -*-
from campaigns.foundation.applet.vote import VoteManager
from campaigns.yiquan.models import Vote, YQWork, WXUser
from campaigns.yiquan.config import VoteConfig
from campaigns.yiquan import app_id


class YiQuanVoteManager(VoteManager):
    def __init__(self):
        super(YiQuanVoteManager, self).__init__(
            app_id=app_id,
            work_class=YQWork,
            vote_class=Vote,
            wx_user_class=WXUser,
            ip_limit_count=VoteConfig.IP_LIMIT_COUNT,
            weixin_limit_count=VoteConfig.WEIXIN_LIMIT_COUNT
        )