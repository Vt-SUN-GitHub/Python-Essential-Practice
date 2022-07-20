from day07.jobBigData.jobBigData.dao.BaseDao import BaseDao

class JobDao(BaseDao):

    def createJobData(self, sql, params):
        result = self.execute(sql, params)
        self.commit()
        return result

    ...