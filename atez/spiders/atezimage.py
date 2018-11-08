# -*- coding: utf-8 -*-
import scrapy
from ..items import AtezItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class AtezimageSpider(CrawlSpider):
    name = 'atezimage'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/3154.html']

    # def parse(self, response):
    #     divs = response.xpath("//div[@class='uibox']")[1:]
    #     for div in divs:
    #         category = div.xpath(".//div[@class='uibox-title']/a/text()").get()
    #         images = div.xpath(".//li/a/img/@src").getall()
    #         image_urls = list(map(lambda url: response.urljoin(url), images))
    #         yield AtezItem(category=category,image_urls=image_urls)
    rules = (
        Rule(LinkExtractor(allow=r"https://car.autohome.com.cn/pic/series/3154.+"), callback='parse_page', follow=True),
    )
    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        images = response. xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        image_urls = list(map(lambda url: response.urljoin(url.replace("t_", "")), images))
        yield AtezItem(category=category, image_urls=image_urls)
