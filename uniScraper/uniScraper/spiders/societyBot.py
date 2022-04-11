import scrapy


class SocietybotSpider(scrapy.Spider):
    name = 'societyBot'
    allowed_domains = ['su.sheffield.ac.uk']
    base_url = ['http://su.sheffield.ac.uk/activities/find-a-society']

    def start_requests(self):
        base_url = 'http://su.sheffield.ac.uk/activities/find-a-society'
        yield scrapy.Request(url=base_url, callback=self.parse)
    
    
    def parse(self, response):
        for row in response.css('.card--title.pdg__b--1'):
            yield {
                'society': (row.css('div::text').get()).strip('\n').lstrip().rstrip(),
            }
