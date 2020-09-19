
import employees

class ProductivitySystem:
    def track (self, employees, hours):
        print(f'Tracking employee productivity')
        print("================================")
        for employee in employees:
            employee.work(hours)

        print(' ')
