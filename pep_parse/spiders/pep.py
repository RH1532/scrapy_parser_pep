import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for link in response.css('tbody tr a[href^="pep-"]'):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        _, number, _, *name = response.css(
            'h1.page-title::text'
        ).get().split()
        data = {
            'number': number,
            'name': ' '.join(name).strip(),
            'status': response.css(
                'dt:contains("Status")+dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
