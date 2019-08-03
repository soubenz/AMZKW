
#coding: utf-8
import scrapy

from scrapy.http import Request
from scrapy.shell import inspect_response
from kwg.items import Keyword
from ast import literal_eval


class GoogleCrawler(scrapy.Spider):
    name = 'google'
    custom_settings = {
        "DEPTH_PRIORITY": 1,
        "SCHEDULER_DISK_QUEUE": 'scrapy.squeues.PickleFifoDiskQueue',
        "SCHEDULER_MEMORY_QUEUE": 'scrapy.squeues.FifoMemoryQueue'
    }

    def __init__(self, keyword="milk", limit=3000, *args, **kwargs):
        super(GoogleCrawler, self).__init__(*args, **kwargs)
        # pass
        self.keyword = keyword.lower()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.youtube.com/',
            'Origin': 'https://www.youtube.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        }
        self.url = "https://www.google.com/complete/search?q={}&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en-FR&authuser=0&pq=suggestions"
        self.limit = limit
        self.position = 1
        self.seen = set()

    def start_requests(self):
        url = self.url.format(self.keyword)
        yield Request(url, self.generate, headers=self.headers, meta={"keyword": self.keyword})

    def generate(self, response):
        raw = response.body.decode('utf-8').lstrip(")]}'")
        l = literal_eval(raw)
        keyword = response.meta["keyword"]
        kws = l[0]

        if len(kws) <= 1:
            return
        else:
            for kw in kws:
                item = Keyword()
                if self.position <= self.limit:

                    kwd = kw[0]
                    item["text"] = kwd.replace('<\\/b>', '').replace('<b>', '')
                    meta = {"keyword": kwd}
                    if item['text'] in self.seen:
                        pass
                    else:
                        self.seen.add(item['text'])
                        self.position += 1
                        yield item

                    if self.position <= self.limit:
                        url = self.url.format(kwd)
                        yield Request(url, self.generate, headers=self.headers, meta=meta)
