# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field
    price = scrapy.Field
    availability = scrapy.Field
    stock_count = scrapy.Field
    num_reviews = scrapy.Field
    url = scrapy.Field
