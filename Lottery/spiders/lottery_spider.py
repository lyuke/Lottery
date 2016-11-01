import scrapy
import lotteryItem from items

class LotteryScrapy(scrapy.Spider):
    name = "lottery"
    allowed_domains = ["dmoz_orgs"]
    start_urls = [
        "http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt"
    ]

    def parse(self, response):
        for sel in response.xpath('//tr[1]'):
            item = lotteryItem()
            item['issue'] = sel.xpath('//td[1]')
            yield item
