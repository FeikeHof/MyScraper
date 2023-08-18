import scrapy


class BoardgameGeekSpider(scrapy.Spider):
    name = "boardgame_geek"
    allowed_domains = ["boardgamegeek.com"]
    start_urls = ["https://boardgamegeek.com/boardgame/224517/brass-birmingham"]

    def parse(self, response: scrapy.http.response.Response, **kwargs):
        with open('reponse.html', 'w') as file:
            print(response.body.decode('utf-8'), file=file)
