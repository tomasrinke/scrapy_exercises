# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project1Item(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
