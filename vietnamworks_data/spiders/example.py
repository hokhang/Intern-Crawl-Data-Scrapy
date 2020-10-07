import scrapy
from scrapy.selector import Selector 
from scrapy.item import Item

class ExampleSpider(scrapy.Spider):
    name = 'example'
    count = 0
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        urls = [
            'https://careerbuilder.vn/viec-lam/cntt-phan-cung-mang-cntt-phan-mem-c63,1-vi.html',
            # 'https://www.topcv.vn/tim-viec-lam-it-phan-cung-mang-c10025?salary=0&exp=0&company_field=0&page=1',
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse, headers = headers)

    def parse(self, response):
        list_url = response.css("a.job_link::attr('href')").extract()
        for list_job in list_url:
            self.count +=1
            yield scrapy.Request(list_job, callback = self.page)

        next_page = response.css('li.next-page a::attr("href")').get()
        # next_page = response.xpath('//*[@id="box-job-result"]/div[2]/nav/ul/li[13]/a/@href').get()
        if next_page is not None:
            print('**************************',self.count)
            
            yield scrapy.Request(next_page, callback = self.parse)

    def page(self, response):
        # print(response.url)
        # print("############################################################")
        detail_titles = response.css('h3.detail-title::text').extract()
        print(detail_titles)
        for detail_title in detail_titles:
            detail_text = detail_title.replace(' ', '')
            if detail_text == 'Phúclợi':
                benefit = response.css('ul.welfare-list::text').extract()
                # get_benefit = benefit.strip()
                print(1)
                print(benefit)
            if detail_text == 'MôtảCôngviệc':
                return 'hihi'
            if detail_text == 'YêuCầuCôngViệc':
                return 'haha'
        

    def close(self,reason):
        print(self.count)
        print("sadaaaaaadadsad")

