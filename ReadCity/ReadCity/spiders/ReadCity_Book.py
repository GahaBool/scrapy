import scrapy


class ReadcityBookSpider(scrapy.Spider):
    name = "ReadCity_Book"
    allowed_domains = ["chitai-gorod.ru"]
    start_urls = ["https://www.chitai-gorod.ru/catalog/books-18030"]

    def parse(self, response):
        for element in response.css('div.products-list'):
            yield{
                'Name' : element.css('article').extract(),
                'Price' : element.css('article').extract()
            }

if __name__ == '__main__':
    print()