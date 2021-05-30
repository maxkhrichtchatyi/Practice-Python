from abc import ABC, abstractmethod


class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("-------------------")
        for employee in employees:
            print(f"Payroll for {employee.id} - {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}\n")


class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


salary_employee = SalaryEmployee(id=1, name="John Smith", weekly_salary=1500)
hourly_employee = HourlyEmployee(
    id=2, name="Rebekka Newman", hour_rate=30, hours_worked=301
)
commission_employee = CommissionEmployee(
    id=3, name="Tom Jones", weekly_salary=1400, commission=350
)

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(
    employees=[
        salary_employee,
        hourly_employee,
        commission_employee,
    ]
)
