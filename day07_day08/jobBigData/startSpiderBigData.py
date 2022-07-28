from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'jobspiders', '-a',
         'baseURL=https://www.liepin.com/zhaopin/?headId=c84f1c65eaf269fba1a742dae999352b&ckId=wi3ejfutjojc0twr4nfm05u75jsipseb&oldCkId=c84f1c65eaf269fba1a742dae999352b&fkId=a2dr3hivx5gp2pw29e7wt8pz03x7rj19&skId=a2dr3hivx5gp2pw29e7wt8pz03x7rj19&sfrom=search_job_pc&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&currentPage={0}&scene=page',
         '-a', 'jobType=大数据'])