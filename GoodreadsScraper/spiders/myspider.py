import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.goodreads.com/book/show/11296523-the-kite-runner']


    def parse(self, response):
        # Save the HTML response to a file
        with open('myspiderresponse.html', 'wb') as f:
            f.write(response.body)