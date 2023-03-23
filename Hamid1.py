import scrapy


class Hamid1Spider(scrapy.Spider):
    name = "Hamid1"
    allowed_domains = ["liliome.ir"]
    start_urls = ["https://liliome.ir/brand/big-size-%d8%a7%d8%af%da%a9%d9%84%d9%86-%d8%b3%d8%a7%db%8c%d8%b2-%d8%a8%d8%b2%da%af/"]

    def parse(self, response):
        aa = response.xpath('//*[@class = "product-small box "]')

        for aa1 in aa:
            title = aa1.xpath('.//*[@class = "woocommerce-LoopProduct-link woocommerce-loop-product__link"]/text()').extract_first()
            price = aa1.xpath('.//*[@class = "woocommerce-Price-amount amount"]//bdi/text()').extract_first()                 
            rating = aa1.xpath('.//*[@class = "rating"]//text()').extract_first()  
            yield{'title':title, 'price':price, 'rating':rating}
                             
        next_page = response.xpath('//*[@class = "next page-number"]/@href').extract_first()
        real_page = response.urljoin(next_page)
        if next_page:
            yield scrapy.Request(real_page, callback=self.parse ) 
        
