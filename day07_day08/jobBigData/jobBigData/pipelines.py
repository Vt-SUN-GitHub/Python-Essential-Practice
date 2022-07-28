# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from day07.jobBigData.jobBigData.dao.JobDao import JobDao

class JobbigdataPipeline:
    def process_item(self, item, spider):

        #工作地点（城市）
        jobAddress = item['jobAddress']
        jobCity = ""
        if jobAddress.find("-") != -1:
            jobCity = jobAddress.split("-")[0]
            ...
        else:
            jobCity = jobAddress
            ...
        #工作薪水(最低，最高，平均)
        jobSalary =item["jobSalary"]
        jobLowSalary = jobHighSalary = jobMeanSalary = 0
        if jobSalary.find("k") != -1:
            jobSalary = jobSalary.split("k")[0]
            if jobSalary.find("-") != -1:
                salaryArray = jobSalary.split("-")
                jobLowSalary = float(salaryArray[0]) * 1000
                jobHighSalary = float(salaryArray[1]) * 1000
                jobMeanSalary = (jobLowSalary + jobHighSalary) / 2
                ...
            else:
                jobLowSalary = jobHighSalary = jobMeanSalary = float(jobSalary) * 1000
                ...
            ...
        if jobMeanSalary > 0:
            sql = 'insert into crawler_job(jobName, jobSalary, jobAddress, jobCompany, jobLink, jobType, jobCity, jobLowSalary, jobHighSalary, jobMeanSalary) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'
            params = [item['jobName'],item['jobSalary'],item['jobAddress'],item['jobCompany'],item['jobLink'], item['jobType'],
                  jobCity, jobLowSalary, jobHighSalary, jobMeanSalary]
            jobDao = JobDao()
            try:
                result = jobDao.createJobData(sql,params)
                if result > 0:
                    print("write successfully")
                    ...
            except Exception as e:
                print(e)
                ...
            finally:
                jobDao.close()
                ...
        return item
