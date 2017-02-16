import scrapy
from scrapy.item import Item, Field


class ThehindudailynewsItem(scrapy.Item):
    # Primary fields
    LINK = Field()
    TITLE = Field()
    SUBHEADING = Field()
    CONTENT = Field()
    CATEGORY = Field()
    # Calculated fields
    IMAGE = Field()
    TAGS = Field()

    # Housekeeping fields
    URL = Field()
    project = Field()
    spider = Field()
    server = Field()
    TIME = Field()
