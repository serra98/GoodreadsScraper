import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.goodreads.com/review/list/11083989-s?shelf=%23ALL%23']


    def parse(self, response):
        # Save the HTML response to a file
        with open('myspiderresponse.html', 'wb') as f:
            f.write(response.body)