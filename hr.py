
class PayrollSystem:
    """
    This class is responsible for calculating the payroll for
    different types of employees in the company
    """
    def calculate_payroll(self, employees):
        """:arg takes in the collection of different types of employess
        and prints the employee name, id and check amount for each employee"""
        print("Calculating the Payroll")
        print("==========================")

        for employee in employees:
            print(f'Payroll for:{employee.id} - {employee.name}')
            print(f'-Check amount:{employee.calculate_payroll()}')
            print(' ')