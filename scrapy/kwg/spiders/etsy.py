
#coding: utf-8
import scrapy

from scrapy.http import Request
from scrapy.shell import inspect_response
from kwg.items import Keyword
import json
from scrapy.selector import Selector

class YoutubeCrawler(scrapy.Spider):
    name = 'etsy'
    custom_settings = {
        "DEPTH_PRIORITY" : 1,
        "SCHEDULER_DISK_QUEUE" : 'scrapy.squeues.PickleFifoDiskQueue',
        "SCHEDULER_MEMORY_QUEUE" : 'scrapy.squeues.FifoMemoryQueue'
    }
    def __init__(self, keyword="milk", limit=3000, *args, **kwargs):
        super(YoutubeCrawler, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.etsy.com/',
            'Origin': 'https://www.etsy.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        }
        self.url = "https://www.etsy.com/suggestions_ajax.php?extras={&quot;expt&quot;:&quot;randomize&quot;,&quot;lang&quot;:&quot;en-US&quot;,&quot;extras&quot;:[]}&version=10_12672349415_19&search_query=%s&search_type=all"
        self.limit = limit
        self.position = 0

    def start_requests(self):
        url = self.url % self.keyword
        yield Request(url, self.generate, headers=self.headers, meta={"keyword": self.keyword, "position":0})

    def generate(self, response):
        js = json.loads(response.body.decode('utf-8'))
        results = js['results']
        keyword = response.meta["keyword"]

        if len(results) <= 1:
            return
        else:
            for kw in results:
                item = Keyword()
                if self.position < self.limit:
                    self.position += 1
                    kwd = kw['query']
                    if 'span' in kwd:
                        s = Selector(text=kwd)
                        kwd = s.css('.shop-suggestion-item::text').get()
                        print(kwd)

                    item["text"] = kwd
                    meta = {"keyword": kwd}
                    yield item
                    if self.position < self.limit:
                        url = self.url % (kwd)
                        yield Request(url, self.generate, headers=self.headers, meta=meta)
