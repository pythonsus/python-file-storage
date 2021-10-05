import scrapy
from ..items import QuotestoscrapeItem
class Quotespider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self,response):
        all_div_quotes = response.css('div.quote')
        for q in all_div_quotes:
            title = q.css('title::text').extract()
            quote = q.css('span.text::text').extract()
            author = q.css('small.author::text').extract()
            tag = q.css('.tag::text').extract()
            yield {'title': title,
            'quotes': quote,
            'author': author,
            'tag': tag
                 }


