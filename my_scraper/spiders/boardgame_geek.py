import scrapy


class BoardgameGeekSpider(scrapy.Spider):
    name = "boardgame_geek"
    allowed_domains = ["boardgamegeek.com"]
    start_urls = ["https://boardgamegeek.com"]

    def parse(self, response):
        with open(response.request.url, 'w') as file:
            print(response.content, file=file)
