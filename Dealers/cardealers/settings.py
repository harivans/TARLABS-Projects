# -*- coding: utf-8 -*-

# Scrapy settings for cardealers project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cardealers'

SPIDER_MODULES = ['cardealers.spiders']
NEWSPIDER_MODULE = 'cardealers.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cardealers (+http://www.yourdomain.com)'
VPN_setting = {
               'username':'tarunlalwani@gmail.com',
               'password':'indian007#',
               'timeout':'30',
               }