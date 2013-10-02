#!/usr/bin/env python

import sys
from os.path import dirname, abspath 

# make weibowrapper accessible in PYTHONPATH
sys.path.append(dirname(dirname(abspath(__file__))))

from weibowrapper import conf
from weibowrapper.shortcuts import *
from weibowrapper.sdk import WeiboAccount

test_profile = WeiboAccount(conf.uid_example, token=conf.token_example)

if __name__ == '__main__':
    sum_test = 0
    print(sum_test)
#    for profile in get_follower(test_profile):
#        sum_test += 1

#    for profile in get_following(test_profile):
#        sum_test += 1

#    for feed in get_all_myfeed(test_profile):
#        sum_test += 1

#    for feed in get_all_archive(test_profile):
#        sum_test += 1

#    for feed in get_all_timeline(test_profile):
#        sum_test += 1

