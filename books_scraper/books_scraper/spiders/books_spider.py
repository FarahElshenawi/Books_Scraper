import scrapy
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls =['https://books.toscrape.com']

    def parse(self, response):
        for book in response.css('article.product_pod'):

            product_url = book.css('h3 a::attr(href)').get()

            yield response.follow(product_url , callback = self.parse_book)


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page , callback = self.parse)

    def parse_book(self, response):
        product_info = {}
        for row in response.css('table.table-striped tr'):
            label = row.css('th::text').get()
            value = row.css('td::text').get()
            if label and value:
                product_info[label] = value

        item = BookItem()
        item['title'] = response.css('h1::text').get()
        item['price'] = response.css('p.price_color::text').get()
        item['availability'] = product_info.get('Availability', '')
        item['upc'] = product_info.get('UPC', '')
        item['num_reviews'] = product_info.get('Number of reviews', '0')
        item['url'] = response.url
        yield item