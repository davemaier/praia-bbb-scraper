# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashFormRequest, SplashRequest
from scrapy_selenium import SeleniumRequest


class RouteSpider(scrapy.Spider):
    name = 'route'


   

    def start_requests(self):
        script = """
                   function main(splash)
                   splash:set_viewport_size(300,700)
                       assert(splash:go(splash.args.url))

                        assert(splash:wait(5))



                        local textfield_from = splash:select('#From')
        	            textfield_from:mouse_click()

                        splash:send_keys('{0}')

                        assert(splash:wait(1))

                        splash:send_keys('<Escape>')
                        assert(splash:wait(0.2))

                        local textfield_to = splash:select('#To')
        	            textfield_to:mouse_click()

                        splash:send_keys('{1}')

                        assert(splash:wait(1))

                        splash:send_keys('<Escape>')
                        assert(splash:wait(0.2))

                        local button_search = splash:select('.hfs_btn.hfs_btnPrimary.hfs_btnBlock')
        	            button_search:mouse_click()

                        assert(splash:wait(5))


                        return {{
                            html = splash:html()
                        }}
                   end
                   """.format(self.address_from, self.address_to)

        yield SplashRequest(
            url='https://verkehrsauskunft.verbundlinie.at/webapp/index.html?L=vs_stv',
            callback=self.parse,
            endpoint='execute',
            args={'lua_source': script})

    def parse(self, response):

        return {
            "travel_time": min(response.xpath('//*[contains(@class, "hfs_infoItem")]/text()').extract()[0::2])
        }
