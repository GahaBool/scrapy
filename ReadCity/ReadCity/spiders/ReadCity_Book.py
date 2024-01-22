import scrapy


class ReadcityBookSpider(scrapy.Spider):
    name = "ReadCity_Book"
    allowed_domains = ["chitai-gorod.ru"]
    start_urls = ["https://www.chitai-gorod.ru/catalog/books-18030"]

    def parse(self, response):


