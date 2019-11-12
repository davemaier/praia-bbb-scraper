# -*- coding: utf-8 -*-
import scrapy


class RouteSpider(scrapy.Spider):
    name = 'route'
    allowed_domains = ['https://verkehrsauskunft.verbundlinie.at']
    start_urls = ['//https://verkehrsauskunft.verbundlinie.at/']

    def parse(self, response):
        pass
