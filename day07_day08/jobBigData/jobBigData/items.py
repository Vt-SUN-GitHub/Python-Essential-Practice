# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobbigdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobSalary = scrapy.Field()
    jobAddress = scrapy.Field()
    jobCompany = scrapy.Field()
    jobLink = scrapy.Field()
    jobType = scrapy.Field()
    pass
