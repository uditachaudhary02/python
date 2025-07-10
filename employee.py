class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

def cal_paycheck(self):
    return 0.0

class SalaryEmployee(Employee): 
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary=salary

    def cal_paycheck(self):
        return self.salary/52
    
class HourEmployee(Employee):
    def __int__(self,fname,lname,weekly_hour,hourly_rate):
        super().__init__(fname,lname)
        self.weekly_hour=weekly_hour
        self.hourly_rate=hourly_rate

    def cal_paycheck(self):
        return self.weekly_hour*self.hourly_rate