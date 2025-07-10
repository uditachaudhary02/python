from employee import Employee,SalaryEmployee,HourEmployee
class company:
    def __init__(self):
        self.employees=[]

    def add_emp(self,new_emp):
        self.employees.append(new_emp)

    def display_emp(self):
        print('current emp')
        for i in self.employees:
            print(i.fname,i.lname)
        print('---------')

    def pay_emp(self):
        print('paying')
        for i in self.employees:
            print('paycheck',i.fname,i.lname)
            #print('Amt',{i.cal_paycheck():,.2f})
            print(f"Amt: {i.cal_paycheck():,.2f}")

            print('-----')


def main():
    my_comp=company()

    emp1=SalaryEmployee('Sara','hess',5000)
    my_comp.add_emp(emp1)
    emp2=HourEmployee('harsh','rawat', 25, 50)
    my_comp.add_emp(emp2)
    emp3=SalaryEmployee('bob','brown',60000)
    my_comp.add_emp(emp3)

    my_comp.display_emp()
    my_comp.pay_emp()

main()
