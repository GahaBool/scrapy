import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
