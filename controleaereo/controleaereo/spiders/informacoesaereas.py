import scrapy


class InformacoesaereasSpider(scrapy.Spider):
    name = 'informacoesaereas'
    #allowed_domains = ['informacoesaereas.com']
    start_urls = ['http://informacoesaereas.com/']

    def parse(self, response):
        # id = q - barra de pesquisa do código ICAO
        informacoesaereas = response.css('#q')
        pass
