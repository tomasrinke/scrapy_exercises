# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from project1.items import Project1Item
from scrapy.contrib.pipeline.files import FilesPipeline
import scrapy

class coeFilesPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.http.Request(url=item["file_urls"]["file_url"], meta={"file_specs": item['file_urls']})

    def file_path(self, request, response=None, info=None):
        return request.meta["file_specs"]["file_name"]