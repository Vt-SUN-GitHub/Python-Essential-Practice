from day07.jobBigData.jobBigData.dao.JobDao import JobDao

jobDao = JobDao()

for item in jobDao.getJobSalaryStatisticByJobCity()[:3]:
    print(item)
    ...

print()

for item in jobDao.getJobSalaryStatisticByJobType():
    print(item)
    ...