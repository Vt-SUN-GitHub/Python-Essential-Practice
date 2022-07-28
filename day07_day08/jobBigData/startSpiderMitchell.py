from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'jobspiders', '-a',
         'baseURL=https://www.liepin.com/zhaopin/?headId=2f25dc2d0991d44ee652f0b99bacb22e&ckId=ylzrg0a0kkvppvm2adz34bb35mdcdkx9&oldCkId=2f25dc2d0991d44ee652f0b99bacb22e&fkId=go5rsuf4r9dqh1vqt92f9fn4fh55ypy8&skId=go5rsuf4r9dqh1vqt92f9fn4fh55ypy8&sfrom=search_job_pc&key=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&currentPage={0}&scene=page',
         '-a', 'jobType=机器学习'])