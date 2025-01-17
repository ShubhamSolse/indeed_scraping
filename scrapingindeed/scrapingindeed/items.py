# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Code written to process data which has been scraped from scrapingindeed.py file
import scrapy

class ScrapingindeedItem(scrapy.Item):
    Company = scrapy.Field()
    JobTitle = scrapy.Field()
    JobLocation = scrapy.Field()
    JobPosted = scrapy.Field()
    CompanyRating = scrapy.Field()
    CompanyReviewCount = scrapy.Field()
    MaxSalary = scrapy.Field()
    MinSalary = scrapy.Field()
    SalaryType = scrapy.Field()
    WorkModel = scrapy.Field()
