import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quote = response.css('div.quote')
        yield{
            'text' : quote.css('span.text::text').get(),
            'author' : quote.css('small.author::text').get()
            }
