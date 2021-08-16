# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StreeteasyItem(scrapy.Item):
    price = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    size = scrapy.Field()
    neighborhood = scrapy.Field()
    listing = scrapy.Field()
    fee = scrapy.Field()
    RentalType = scrapy.Field()