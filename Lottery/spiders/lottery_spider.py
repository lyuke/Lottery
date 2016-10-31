import scrapy

class LotteryScrapy(scrapy.Spider):
    name = "lottery"
    allowed_domains = ["dmoz_orgs"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        print response.body
