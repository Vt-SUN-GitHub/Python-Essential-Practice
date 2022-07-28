from day07_day08.jobBigData.jobBigData.dao.BaseDao import BaseDao

baseDao = BaseDao()

baseDao.execute("select * from userinfo")
print(baseDao.fetchAll())
baseDao.close()