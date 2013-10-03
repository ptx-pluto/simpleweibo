#!/usr/bin/env python
#=============================================================================================

import sys
from os.path import dirname, abspath, join

PATH_UTILS = dirname(dirname(abspath(__file__)))
PATH_ROOT  = dirname(PATH_UTILS)
PATH_APPS  = join(PATH_ROOT, 'apps')
sys.path.append(PATH_ROOT)
sys.path.append(PATH_APPS)
sys.path.append(PATH_UTILS)

from weibowrapper import conf
from weibowrapper.shortcuts import *
from weibowrapper.sdk import WeiboAccount
from weibowrapper.update_db import fetch_data

#=============================================================================================

test_profile = WeiboAccount(conf.uid_example, token=conf.token_example)

#=============================================================================================
# tests for shortcuts
#=============================================================================================

def hello():
    count = 0
    for feed in get_all_archive(test_profile):
        count += 1
    print(count)

#=============================================================================================
# tests for update_db
#=============================================================================================

#=============================================================================================

if __name__ == '__main__':
    pass
