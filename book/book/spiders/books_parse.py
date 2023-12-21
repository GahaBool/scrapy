import scrapy
import json
from scrapy import cmdline

class BooksParseSpider(scrapy.Spider):
    name = "books_parse"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):

        for books in response.css('article.product_pod'):
            yield{
                'Name_book' : books.css('h3 > a::attr(title)').get(default = "not_found"),
                'Price' : books.css('p.price_color::text').get(default = "not_found"),
                'img' : response.css("div.image_container > a > img::attr(src)").get(default = "not_found")
            }

            yield from response.follow_all(css="ul.pager a", callback=self.parse)

def StartProject():
    cmdline.execute("scrapy crawl books_parse -o book.json -t json".split())

def ReadJson():
    with open("book.json", 'r'):
        data = json.load(file)

    for elen in data:
        price = (data["Price"][2:])
    print(price)

if __name__ == "__main__":
    StartProject()

