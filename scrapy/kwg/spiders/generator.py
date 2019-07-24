
#coding: utf-8
import scrapy

from scrapy.http import Request
from scrapy.shell import inspect_response
import sys
import json
import requests
from kwg.items import AmazonKeyword
import time
import hashlib
from random import randint
import re
from datetime import date
from collections import OrderedDict
from pprint import pprint



class HashtagCrawler(scrapy.Spider):
    name = 'generator'
    custom_settings = {
        "DEPTH_PRIORITY" : 1,
        "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
        "SCHEDULER_MEMORY_QUEUE" : 'scrapy.squeues.FifoMemoryQueue'
    }
    def __init__(self, keyword="milk", limit=3, *args, **kwargs):
        super(HashtagCrawler, self).__init__(*args, **kwargs)
        # pass
        self.keyword = keyword.lower()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.amazon.com/',
            'Origin': 'https://www.amazon.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        }
        self.url = "https://completion.amazon.com/api/2017/suggestions?page-type=Gateway&lop=en_US&site-variant=desktop&client-info=amazon-search-ui&mid=ATVPDKIKX0DER&alias=aps&suggestion-type=keyword&b2b=1&prefix={}"
        self.limit = limit
        self.position = 0

    def start_requests(self):
        url = self.url.format(self.keyword)
        yield Request(url, self.generate, headers=self.headers, meta={"keyword": self.keyword, "position":0})

    def generate(self, response):
        js = json.loads(response.text)
        keyword = response.meta["keyword"]
        level = response.meta.get('level', 0)
        if len(js["suggestions"]) <= 1:
            return
        else:
            for kw in js["suggestions"]:
                
                item = AmazonKeyword()

                if kw['value'] != keyword and self.position < self.limit:

                    self.position += 1
                    kwd = kw['value']
                    # self.logger.info(kwd)
                    item["text"] = kwd
                    level += 1
                    meta = {"keyword": kw['value'], "level": level }
                    url = self.url.format(kwd)
                    yield item
                    if self.position < self.limit:
                        yield Request(url, self.generate, headers=self.headers, meta=meta)
            

            # # print(position)
            # for kw in js["suggestions"]:
            #     # if position < self.limit:
                