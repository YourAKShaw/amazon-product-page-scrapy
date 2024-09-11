import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.in']
    start_urls = [
        'https://www.amazon.in/Apple-AirPods-Generation-MagSafe-USB%E2%80%91C/dp/B0CHX719JD/ref=sr_1_3'
    ]

    def parse(self, response):
        # Extract data from the page
        title = response.xpath('//span[@id="productTitle"]/text()').get().strip()
        price = response.xpath('//span[@class="a-price-whole"]/text()').get()
        rating = response.xpath('//span[@id="acrPopover"]/@title').get()
        review_count = response.xpath('//span[@id="acrCustomerReviewText"]/text()').get()

        # Store the extracted data in a dictionary
        yield {
            'title': title,
            'price': price,
            'rating': rating,
            'review_count': review_count
        }
