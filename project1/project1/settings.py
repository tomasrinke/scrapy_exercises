# -*- coding: utf-8 -*-

# Scrapy settings for project1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import scrapy
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'project1'

SPIDER_MODULES = ['project1.spiders']
NEWSPIDER_MODULE = 'project1.spiders'
ITEM_PIPELINES = {'project1.pipelines.coeFilesPipeline': 1}
FILES_STORE = PROJECT_ROOT +'/my_files'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'project1 (+http://www.yourdomain.com)'
