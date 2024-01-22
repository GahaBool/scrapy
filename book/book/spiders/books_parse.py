import scrapy
import json
import os
from scrapy.crawler import CrawlerProcess
import warnings
from tqdm import tqdm
import time

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

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        runner = BooksParseSpider()
    process = CrawlerProcess(settings={
        "FEEDS": {
            "book.json": {"format": "json"},
        },
    })

    process.crawl(BooksParseSpider)
    process.start()


def Size_isempty():
    isempty = os.stat('book.json').st_size
    print(isempty)

def clear_file():
    with open("book.json", 'w') as file:
        file.write("")
    if os.stat('book.json').st_size == 0:
        print("Чисто")
    else:
        print("Что пошло не так!")

def ReadFile():
    with open("book.json", 'r') as file:
        data = json.load(file)

    for elen in data:
        price = (data["Price"][2:])
    print(price)

def End():
    print("Two option")

menu = {'1' : StartProject, '2' : Size_isempty, '3' : clear_file, '4' : ReadFile, '5' : End}


while True:

    options = menu.keys()
    for entry in options:
        print(entry)

    selection = input("Выберите опции: ")

    if selection == '1' or selection == '2' or selection == '3' or selection == '4':
        menu[selection]()
    elif selection == '5':
        print("Пока")
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз")


