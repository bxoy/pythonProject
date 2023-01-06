import scrapy
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # 项目的唯一名字用来区分不同的spider
    allowed_domains = ['quotes.toscrape.com']  # 允许爬取的域名，如果初始或后续的请求链接不是这个域名下的，则请求连接会被过滤掉
    start_urls = ['http://quotes.toscrape.com/']  # 包含了spider在启动时爬取的url列表

    def parse(self, response):  # spider的一个方法
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.xpath('.//*[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            item['tags'] = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url)
