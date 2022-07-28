from day07.jobBigData.jobBigData.dao.BaseDao import BaseDao

class JobDao(BaseDao):

    def createJobData(self, sql, params):
        result = self.execute(sql, params)
        self.commit()
        return result

    def getJobSalaryStatisticByJobCity(self):
        sql = "select AVG(jobMeanSalary) as jobAvgCity, jobCity from crawler_job where jobType = '大数据' GROUP by jobCity ORDER BY jobAvgCity DESC;"
        self.execute(sql)
        return self.fetchAll()

    def  getJobSalaryStatisticByJobType(self):
        sql = "select AVG(jobMeanSalary) as jobAvgCity, jobType from crawler_job GROUP by jobType ORDER BY jobAvgCity DESC;"
        self.execute(sql)
        return self.fetchAll()
    ...