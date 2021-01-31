import scrapy

class ListingSpider(scrapy.Spider):
    name = "Listings"
    start_urls = ["https://blog.scrapinghub.com"]


    def parse(self,response):

        for listing in  response.css('div.post-listing'):
            try:
                yield {
                    'listing_name':listing.css('div.post-header').css('a::text').get(),
                    'url_link': listing.css('a.hs-featured-image-link::attr(href)').get()

                }

            except:
                yield {
                    'listing_name':'__empty__',
                    'url_link':'__empty__'
                }

        # Checking if there's a next page
        next_page = response.css('div.blog-pagination').css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)