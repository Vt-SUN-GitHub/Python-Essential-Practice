import scrapy
from day07.jobBigData.jobBigData.items import JobbigdataItem

class JobspidersSpider(scrapy.Spider):
    name = 'jobspiders'
    # allowed_domains = ['www.baidu.com'] #限制爬取的域名
    page = 0
    baseURL = ''
    start_urls = []

    def __init__(self, baseURL, jobType, *args, **kwargs):
        super(JobspidersSpider, self).__init__(*args, **kwargs)
        JobspidersSpider.baseURL = baseURL
        JobspidersSpider.start_urls.append(JobspidersSpider.baseURL.format(JobspidersSpider.page))
        self.jobType = jobType
        ...


    def parse(self, response):
        # print("第" + str(JobspidersSpider.page + 1) + "页数据")
        selectorList = response.xpath("//div[@class='job-list-item']")
        for item in selectorList:
            pipItem = JobbigdataItem()
            #工作简称
            jobName = item.xpath("./div/div/div/a/div/div/div/text()").extract()[0]
            # print("jobName: " + jobName)
            #工作薪资
            jobSalary = item.xpath("./div/div/div/a/div/span[@class='job-salary']/text()").extract()[0]
            # print("\tsalary: " + jobSalary)
            #工作地点
            jobAddress = item.xpath("./div/div/div/a/div/div/div/span[@class='ellipsis-1']/text()").extract()[0]
            # print("\taddress: " + jobAddress)
            #公司名称
            data = item.xpath("./div/div/div/a[2]/div[@class='job-detail-company-box']/div[@class='job-company-info-box']/span[@class='company-name ellipsis-1']/text()").extract()
            if data: #有链接版
                jobCompany = data[0]
                # print("\tjobCompany: " + jobCompany)
            else:
                jobCompany = item.xpath("./div/div/div/div[@class='job-detail-company-box']/div[@class='job-company-info-box']/span[@class='company-name ellipsis-1']/text()").extract()[0]
                # print("\tjobCompany: "+ jobCompany)
                ...
            #工作详情链接
            jobLink = item.xpath("./div/div/div/a/@href").extract()[0]
            # print("\tjobLink: " + jobLink)
            #招聘要求基本点
            basicRequirement = item.xpath("./div/div/div/a/div[@class='job-labels-box']/span[@class='labels-tag']/text()").extract()
            # print("\tbasic requirement: " + str(basicRequirement))
            pipItem['jobName'] = jobName
            pipItem['jobSalary'] = jobSalary
            pipItem['jobAddress'] = jobAddress
            pipItem['jobCompany'] = jobCompany
            pipItem['jobLink'] = jobLink
            pipItem['jobType'] = self.jobType
            yield pipItem
            ...
        JobspidersSpider.page += 1
        #分页采集
        nextPageUrl = JobspidersSpider.baseURL.format(JobspidersSpider.page)
        yield scrapy.Request(url=nextPageUrl, callback=self.parse, dont_filter=True)
        pass
