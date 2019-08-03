

# -*- coding: utf-8 -*-

from scrapyrt.core import CrawlManager
from scrapyrt.resources import CrawlResource


class MyCrawlResource(CrawlResource):

    def prepare_crawl(self, api_params, scrapy_request_args, *args, **kwargs):
        """Schedule given spider with CrawlManager.
        :param dict api_params:
            arguments needed to find spider and set proper api parameters
            for crawl (max_requests for example)
        :param dict scrapy_request_args:
            should contain positional and keyword arguments for Scrapy
            Request object that will be created
        """
        spider_name = self.get_required_argument(api_params, 'spider_name')
        start_requests = api_params.get("start_requests", False)
        try:
            max_requests = api_params['max_requests']
        except (KeyError, IndexError):
            max_requests = None

        crawler_params = api_params.copy()
        for api_param in ['max_requests', 'start_requests', 'spider_name',
                            'url']:
            crawler_params.pop(api_param, None)
        kwargs.update(crawler_params)

        dfd = self.run_crawl(
            spider_name, scrapy_request_args, max_requests,
            start_requests=start_requests, *args, **kwargs)
        dfd.addCallback(
            self.prepare_response, request_data=api_params, *args, **kwargs)
        # print(dfd.__code__.co_varnames)
        # print(dfd.__code__.co_varnames)
        return dfd

    def prepare_response(self, result, *args, **kwargs):
        response = super().prepare_response(result, *args, **kwargs)
        # response.update({'before' : 23}  )
        response.pop('items_dropped', None)
        return response


class MyCrawlManager(CrawlManager):
    pass
    # def return_items(self, result):
    #     results = super().return_items(result)
    #     items = [item['text'] for item in results['items']]
    #     results.update({'items': items})
    #     return results
