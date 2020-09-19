"""
The HR system needs to process payroll for the company employees for different types of employees
depending on which the payroll is calculated
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Employee is an abstract class which models the abstract representation for Employee
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate


    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary


    def calculate_payroll(self):
        return self.weekly_salary

class CommisionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commision):
        super().__init__(id, name, weekly_salary)
        self.commision = commision

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision

class Manager(SalaryEmployee):
    def __init__(self, id, name, weekly_salary):
        super(Manager, self).__init__(id, name, weekly_salary)
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours for doing office paper work')

class SalesPerson(CommisionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours')












