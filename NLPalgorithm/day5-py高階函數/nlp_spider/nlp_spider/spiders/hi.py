import scrapy


class HiSpider(scrapy.Spider):
    name = "hi"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = ["https://tieba.baidu.com/f?ie=utf-8&kw=%E5%BF%AB%E6%A8%82&fr=search"]

    def parse(self, response):
        # 搜尋的title
        url_list = response.css('.j_th_tit::attr(href)').extract()
        for url in url_list:
            print(url)
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

    def parse_detail(self, response):
        # 帖子的主題
        title = response.css('.core_title_txt.pull-left.text-overflow::text').extract()


        # 作者, 變量為一個list
        authors = response.css('.p_author_name.j_user_card::text').extract()
        # 帖子回復的內容, 需進一步處理
        contents = response.css('.d_post_content.j_d_post_content').extract()
        # 處理帖子的內容, 包含圖片地址, 以及前端的換行標籤      
        content_list = self.get_content(contents)

        # 進一步處理帖子的發送時間, 和所發布的樓數  
        bbs_sendtime_list, bbs_floor_list = self.get_send_time_and_floor(response)




