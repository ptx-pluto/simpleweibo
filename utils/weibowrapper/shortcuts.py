#!/usr/bin/env python
# -*- utf-8 -*-
#=====================================================================================

import os
import math
import json

from whoosh.index import create_in
from whoosh.fields import *
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser
    
from weibowrapper import sdk, conf
from weibowrapper.sdk import WeiboAccount

#=====================================================================================
# get_all_x Shortcuts
#=====================================================================================

def get_follower(account):
    in_progress = True
    query = {'count': 200}
    follower_list = []
    while (in_progress):
        result = account.call_api(conf.API_FOLLOWER, query)
        for profile in result['users']:
            yield profile
        query['cursor'] = result['next_cursor']
        in_progress = (result['next_cursor'] != 0)


def get_following(account):
    in_progress = True
    query = {'count': 200}
    following_list = []
    while (in_progress):
        result = account.call_api(conf.API_FOLLOWING, query)
        for profile in result['users']:
            yield profile
        query['cursor'] = result['next_cursor']
        in_progress = result['next_cursor'] is not 0


def get_all_myfeed(account):
    first_round = True
    total_page = 0
    query = {'count': 100, 'page': 1}
    while (first_round or total_page >= query['page']):
        result = account.call_api(conf.API_MYFEED, query)
        if first_round:
            total_page = math.ceil(result['total_number']/100)
            first_round = False
        for feed in result['statuses']:
            yield feed
        query['page'] += 1


def get_all_archive(account):
    query = {'count':50, 'page': 1}
    first_round = True
    total_page = 0
    while (first_round or total_page >= query['page']):
        result = account.call_api(conf.API_ARCHIVE, query)
        if first_round:
            total_page = math.ceil(result['total_number']/50)
            first_round = False
        for entry in result['favorites']:
            yield entry['status']
        query['page'] = query['page'] + 1


def get_all_timeline(acocunt):
    in_progress = True
    query = {'count': 100}
    while (in_progress):
        result = acocunt.call_api(conf.API_TIMELINE, query)
        for feed in result['statuses']:
            yield feed
        query['max_id'] = result['next_cursor']
        in_progress = result['next_cursor'] != 0

#=====================================================================================
# Search Functionality
#=====================================================================================

def index_db():
    schema = Schema( path     = TEXT(stored=True),
                     tweet_id = ID(stored=True),
                     content  = TEXT,
                     retweet  = TEXT )

    if not os.path.exists(conf.PATH_INDEX):
        os.mkdir(conf.PATH_INDEX)
    my_index = create_in(conf.PATH_INDEX, schema)
    my_writer = my_index.writer()

    for uid in os.listdir(conf.PATH_FEED_DB):
        for tweet in os.listdir(conf.PATH_FEED_DB+'/'+uid):
            rel_path = '/' + uid + '/' + tweet
            with open(conf.PATH_FEED_DB+rel_path, 'r') as f:
                doc = json.loads(f.read())
            if 'retweeted_status' in doc:
                my_writer.add_document( 
                    path     = rel_path, 
                    tweet_id = str(doc['id']), 
                    content  = doc['text'],
                    retweet  = doc['retweeted_status']['text'])
            else:
                my_writer.add_document( 
                    path     = rel_path, 
                    tweet_id = str(doc['id']), 
                    content  = doc['text'],
                    retweet  = '')                
    my_writer.commit()

def search_db(query_str):    
    my_index = open_dir(conf.PATH_INDEX)
    with my_index.searcher() as searcher:
        mparser = MultifieldParser(['content','retweet'], schema=my_index.schema)
        query = mparser.parse(query_str)
        results = searcher.search(query)
        feeds = []
        for path in [entry['path'] for entry in results]:
            with open(conf.PATH_FEED_DB+path,'r') as f:
                feeds.append(json.loads(f.read()))
        return feeds

def index_myfeed():
    schema = Schema( feed_id = ID(stored=True),
                     content = TEXT, 
                     retweet = TEXT)

    if not os.path.exists(conf.PATH_INDEX_MYFEED):
        os.mkdir(conf.PATH_INDEX_MYFEED)

    my_index = create_in(conf.PATH_INDEX_MYFEED, schema)
    my_writer = my_index.writer()
    with open(conf.PATH_MYFEED_JSON, 'r') as f:
        feeds = json.loads(f.read())
        for feed in feeds:
            if 'retweeted_status' in feed:
                my_writer.add_document( 
                    feed_id = str(feed['id']), 
                    content = feed['text'],
                    retweet = feed['retweeted_status']['text'])
            else:
                my_writer.add_document( 
                    feed_id = str(feed['id']), 
                    content = feed['text'],
                    retweet = '')
    my_writer.commit()

def search_myfeed(query_str):
    my_index = open_dir(conf.PATH_INDEX_MYFEED)
    with my_index.searcher() as searcher:
        mparser = MultifieldParser(['content','retweet'], schema=my_index.schema)
        query = mparser.parse(query_str)
        results = searcher.search(query)
        result_list = [entry['feed_id'] for entry in results]
        with open(conf.PATH_MYFEED_JSON,'r') as f:
            feeds = json.loads(f.read())
            return [feed for feed in feeds if str(feed['id']) in result_list]

def index_archive():
    schema = Schema( feed_id = ID(stored=True),
                     content = TEXT, 
                     retweet = TEXT)

    if not os.path.exists(conf.PATH_INDEX_ARCHIVE):
        os.mkdir(conf.PATH_INDEX_ARCHIVE)

    my_index = create_in(conf.PATH_INDEX_MYFEED, schema)
    my_writer = my_index.writer()
    with open(conf.PATH_ARCHIVE_JSON, 'r') as f:
        feeds = json.loads(f.read())
        for feed in feeds:
            if 'retweeted_status' in feed:
                my_writer.add_document( 
                    feed_id = str(feed['id']), 
                    content = feed['text'],
                    retweet = feed['retweeted_status']['text'])
            else:
                my_writer.add_document( 
                    feed_id = str(feed['id']), 
                    content = feed['text'],
                    retweet = '')
    my_writer.commit()

def search_my_archive(query_str):
    my_index = open_dir(conf.PATH_INDEX_ARCHIVE)
    with my_index.searcher() as searcher:
        mparser = MultifieldParser(['content','retweet'], schema=my_index.schema)
        query = mparser.parse(query_str)
        results = searcher.search(query)
        result_list = [entry['feed_id'] for entry in results]
        with open(conf.PATH_ARCHIVE_JSON,'r') as f:
            feeds = json.loads(f.read())
            return [feed for feed in feeds if str(feed['id']) in result_list]
