import scrapy
from Lottery.items import LotteryItem

class LotteryScrapy(scrapy.Spider):
    name = "lottery"
    allowed_domains = ["dmoz_orgs"]
    start_urls = [
        "http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt"
    ]

    def parse(self, response):
            for sel in response.xpath('//tbody//tr'):
                item = LotteryItem()
                item['issue'] = sel.xpath('td[1]/text()').extract()
                item['frontNumberOne'] = sel.xpath('td[2]/text()').extract()
                item['frontNumberTwo'] = sel.xpath('td[3]/text()').extract()
                item['frontNumberThree'] = sel.xpath('td[4]/text()').extract()
                item['frontNumberFour'] = sel.xpath('td[5]/text()').extract()
                item['frontNumberFive'] = sel.xpath('td[6]/text()').extract()
                item['backNumberOne'] = sel.xpath('td[7]/text()').extract()
                item['backNumberTwo'] = sel.xpath('td[8]/text()').extract()
                item['openDate'] = sel.xpath('td[20]/text()').extract()
                yield item
