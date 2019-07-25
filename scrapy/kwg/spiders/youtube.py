
#coding: utf-8
import scrapy

from scrapy.http import Request
from scrapy.shell import inspect_response
from kwg.items import Keyword
from ast import literal_eval


class YoutubeCrawler(scrapy.Spider):
    name = 'youtube'
    custom_settings = {
        "DEPTH_PRIORITY" : 1,
        "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
        "SCHEDULER_MEMORY_QUEUE" : 'scrapy.squeues.FifoMemoryQueue'
    }
    def __init__(self, keyword="milk", limit=3000, *args, **kwargs):
        super(YoutubeCrawler, self).__init__(*args, **kwargs)
        # pass
        self.keyword = keyword.lower()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.youtube.com/',
            'Origin': 'https://www.youtube.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        }
        self.url = "https://clients1.google.com/complete/search?client=youtube&hl=en&gl=fr&gs_rn=64&gs_ri=youtube&ds=yt&cp=8&gs_id=w&q={}"
        self.limit = limit
        self.position = 0

    def start_requests(self):
        url = self.url.format(self.keyword)
        yield Request(url, self.generate, headers=self.headers, meta={"keyword": self.keyword, "position":0})

    def generate(self, response):
        raw = response.body.decode('utf-8').strip('window.google.ac.h').strip('()')
        l = literal_eval(raw)
        keyword = response.meta["keyword"]
        kws = l[1]

        if len(kws) <= 1:
            return
        else:
            for kw in kws:
                item = Keyword()
                if self.position < self.limit:
                    self.position += 1
                    kwd = kw[0]
                    item["text"] = kwd
                    meta = {"keyword": kwd}
                    yield item
                    if self.position < self.limit:
                        url = self.url.format(kwd)
                        yield Request(url, self.generate, headers=self.headers, meta=meta)
