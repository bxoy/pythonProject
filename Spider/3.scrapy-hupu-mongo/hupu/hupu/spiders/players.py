import scrapy
from hupu.items import HupuItem


class PlayersSpider(scrapy.Spider):
    name = 'players'
    allowed_domains = ['nba.hupu.com']
    start_urls = ['https://nba.hupu.com/stats/players']

    def parse(self, response):
        item = HupuItem()
        players = response.xpath('//*[@id="data_js"]/div[4]/div/table/tbody//tr')
        for player in players[1:]:
            item['name'] = player.xpath('./td[2]//text()')[0]
            item['team'] = player.xpath('./td[3]//text()')[0]
            item['score'] = player.xpath('./td[4]//text()')[0]
            item['accuracy'] = player.xpath('./td[6]//text()')[0]
            yield item
