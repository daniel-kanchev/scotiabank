import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from scotiabank.items import Article


class ScotiaSpider(scrapy.Spider):
    name = 'scotia'
    allowed_domains = ['tc.scotiabank.com']
    start_urls = ['https://tc.scotiabank.com/about-scotiabank/media-centre.html']

    def parse(self, response):
        paragraphs = response.xpath('(//div[@class="cmp cmp-text"])[2]/p')
        paragraphs = [p for p in paragraphs if p.xpath('.//text()').get().strip()
                      and not p.xpath('.//text()').get().startswith('[')]

        current_date = ''
        for p in paragraphs:
            if not p.xpath('.//a').get():
                current_date = p.xpath('.//text()').get()[:-1]
            else:
                item = ItemLoader(Article())
                item.default_output_processor = TakeFirst()

                title = p.xpath('.//a/text()').get()
                link = p.xpath('.//a/@href').get()

                item.add_value('title', title)
                item.add_value('date', current_date)
                item.add_value('link', response.urljoin(link))

                yield item.load_item()
