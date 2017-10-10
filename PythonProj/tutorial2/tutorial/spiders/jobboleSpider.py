import scrapy
import re
from scrapy.http import Request
from urllib import parse
from tutorial.items import jobboleItem

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains= ["blog.jobbole.com"]
    start_urls = ["http://blog.jobbole.com/all-posts/"]

    def parse(self, response):
        # 获取文章列表页中所有的url，交给scrapy解析
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
             image_url = post_node.css('img::attr(src)').extract_first("")
             post_url = post_node.css('::attr(href)').extract_first("")
             yield Request(parse.urljoin(response.url, post_url), meta={"front_image_url":image_url},
                          callback=self.parse_detail)

        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]
        if next_url:
            yield Request(parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 文章标题

        front_image_url = response.meta.get("front_image_url", "")
        print(front_image_url)
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # 创作时间
        create_date = response.xpath('//div[@class="entry-meta"]/p/text()').extract()[0].strip().replace(" ·", "")
        # 点赞数
        praise_nums = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract()[0]

        # 收藏数
        fav_nums = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        # 获得 数字
        re_match = re.match(".*?(\d+).*", fav_nums)
        if re_match:
            fav_nums = re_match.group(1)
        else:
            fav_nums = 0

        # 评论数
        comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        # 获得 数字
        re_match = re.match(".*?(\d+).*", comment_nums)
        if re_match:
            comment_nums = re_match.group(1)
        else:
            comment_nums = 0

        # 标签
        # tags = response.css('')

        print(title, create_date, fav_nums, praise_nums, comment_nums)

        jobbole_item = jobboleItem()  # 创建Item实例对象
        jobbole_item['title'] = title
        jobbole_item['create_date'] = create_date
        jobbole_item['fav_nums'] = fav_nums
        jobbole_item['praise_nums'] = praise_nums
        jobbole_item['comment_nums'] = comment_nums
        jobbole_item['front_image_url'] = [front_image_url]
        # jobbole_item['front_image_path'] =
        # jobbole_item['url_object_id'] =
        jobbole_item['url'] = response.url
        # jobbole_item['tags'] = tags
        yield jobbole_item



