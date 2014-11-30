__author__ = 'hali'

import employee
class Staff(object):

    def __init__(self):
        self.employee_list = []

    def add_employee(self,
                     name,
                     number,
                     years_worked,
                     salary):

        new_emp = employee.Employee(name,
                                    number,
                                    years_worked,
                                    salary)
        self.employee_list.append(new_emp)
