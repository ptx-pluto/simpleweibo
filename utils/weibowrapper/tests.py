#!/usr/bin/env python

import conf
from weibowrapper.shortcuts import *
from sdk import WeiboAccount

test_profile = WeiboAccount(conf.uid_example, token=conf.token_example)

if __name__ == '__main__':
    for profile in get_follower(test_profile):
        pass

    for profile in get_following(test_profile):
        pass

    for feed in get_all_myfeed(test_profile):
        pass

    for feed in get_all_archive(test_profile):
        pass

    for feed in get_all_timeline(test_profile):
        pass
