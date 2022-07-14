'''
员工工资计算
    说明：公司所有员工的底薪一致（5000），不同岗位有不同的岗位工资。
    同时每月也有绩效工资。所以月度应发工资的组成 = 底薪 + 岗位工资 + 绩效工资。
    但实际发放时根据总数扣除相应的保险及公积金等税。
    社会保险：应发总额 * 3%
    公积金：应发总额 * 3%
    月度实发工资 = 月度应发工资 - 社会保险费用 - 公积金费用
    实现1（必做）：创建父类Employee员工类，定义底薪salary属性（全员一致）
    实现2（必做）：创建子类Manager部门经理类，继承Employee父类，同时该类有自己的岗位工资worksalary 2000元 + 绩效工资 jxsalay (每月不确定，根据月度工作考评确定)。
    实现3（选做）：同时在Manager类中定义一个方法calcSalary（）按照 月度应发工资公式计算出当月经理的应发月度工资。
    实现4：（选做）：创建经理类对象，输出月度绩效，最终输出经理的月度应发工资和实发工资
'''

class Employee(object):

    def __init__(self, salary = 5000):
        self._salary = salary
        ...

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary
        ...
    ...

class Manager(Employee):

    def __init__(self, jxSalary, workSalary = 2000):
        super().__init__()
        self.__workSalary = workSalary
        self.__jxSalary = jxSalary
        ...

    def calcSalary(self):
        return (self._salary + self.__workSalary +self.__jxSalary)

    def take_home_pay(self):
        return self.calcSalary()*0.94

    ...

if __name__ == '__main__':
    manager = Manager(10000)
    print("经理的月度应发工资为: " +(str)(manager.calcSalary()))
    print("经理的月度实发工资为: "+(str)(manager.take_home_pay()))


