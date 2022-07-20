from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'jobspiders', '-a',
         'baseURL=https://www.liepin.com/zhaopin/?headId=9137aa4c4023d600e91afbb63956dd4b&ckId=65kxcstgwvpj9vari7ie82dcpf7n8xqb&oldCkId=9137aa4c4023d600e91afbb63956dd4b&fkId=nr7yrt802916ino6e3t5ppp8b3sqpema&skId=nr7yrt802916ino6e3t5ppp8b3sqpema&sfrom=search_job_pc&key=Java&currentPage={0}&scene=page',
         '-a', 'jobType=Java'])