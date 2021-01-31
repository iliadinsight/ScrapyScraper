'''
Taken from https://www.tutorialspoint.com/scrapy/scrapy_following_links.htm
'''
import scrapy

class PostsSpider(scrapy.Spider):
    name = "Post"
    start_urls = ["https://blog.scrapinghub.com"]

    def parse(self,response):
        for listing in  response.css('div.post-listing'):
            url = listing.css('a.hs-featured-image-link::attr(href)').get()
            yield scrapy.Request(url,callback=self.parse_post_contents)

    def parse_post_contents(self,response):
        yield {
            'title':response.css('span.hs_cos_wrapper::text').get(),
            'date': response.css('span.date').css('a::text').get(),
            'author': response.css('span.author').css('a::text').get(),
            'no_comment': response.css('span.custom_listing_comments').css('a::text').get(),
            #'content': response.css('div.section.post-body').css('p').getall()
        }