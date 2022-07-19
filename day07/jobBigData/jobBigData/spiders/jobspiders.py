import scrapy


class JobspidersSpider(scrapy.Spider):
    name = 'jobspiders'
    # allowed_domains = ['www.baidu.com'] #限制爬取的域名
    start_urls = ['https://www.liepin.com/zhaopin/?inputFrom=www_index&workYearCode=0&key=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&scene=input&ckId=go5rsuf4r9dqh1vqt92f9fn4fh55ypy8']

    def parse(self, response):
        selectorList = response.xpath("//div[@class='job-list-item']")
        for item in selectorList:
            #工作简称
            jobName = item.xpath("./div/div/div/a/div/div/div/text()").extract()[0]
            print("jobName: " + jobName)
            #工作薪资
            jobSalary = item.xpath("./div/div/div/a/div/span[@class='job-salary']/text()").extract()[0]
            print("\tsalary: " + jobSalary)
            #工作地点
            jobAddress = item.xpath("./div/div/div/a/div/div/div/span[@class='ellipsis-1']/text()").extract()[0]
            print("\taddress: " + jobAddress)
            #公司名称
            data = item.xpath("./div/div/div/a[2]/div[@class='job-detail-company-box']/div[@class='job-company-info-box']/span[@class='company-name ellipsis-1']/text()").extract()
            if data: #有链接版
                jobCompany = data[0]
                print("\tjobCompany: " + jobCompany)
            else:
                jobCompany = item.xpath("./div/div/div/div[@class='job-detail-company-box']/div[@class='job-company-info-box']/span[@class='company-name ellipsis-1']/text()").extract()[0]
                print("\tjobCompany: "+ jobCompany)
                ...
            #工作详情链接
            jobLink = item.xpath("./div/div/div/a/@href").extract()[0]
            print("\tjobLink: " + jobLink)
            #招聘要求基本点
            basicRequirement = item.xpath("./div/div/div/a/div[@class='job-labels-box']/span[@class='labels-tag']/text()").extract()
            print("\tbasic requirement: " + str(basicRequirement))
            ...
        pass
