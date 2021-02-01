'''
Taken from https://www.tutorialspoint.com/scrapy/scrapy_following_links.htm
'''
import scrapy

class PostsSpider(scrapy.Spider):
    name = "Post"
    start_urls = ["https://blog.scrapinghub.com"]

    def parse(self,response):

        post_links = response.css('div.post-listing').css('a.hs-featured-image-link::attr(href)').getall()
        yield from response.follow_all(post_links, self.parse_post)

    def parse_post(self,response):
        yield {
            'url':response.url,
            'title':response.css('span.hs_cos_wrapper::text').get(),
            'date': response.css('span.date').css('a::text').get(),
            'author': response.css('span.author').css('a::text').get(),
            'no_comment': response.css('span.custom_listing_comments').css('a::text').get(),
            'content': response.css('span.hs_cos_wrapper.hs_cos_wrapper_meta_field.hs_cos_wrapper_type_rich_text').css('span::text').getall()
        }