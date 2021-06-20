from hr import PayrollSystem
from employees import Manager, Secretary, SalesPerson, FactoryWorker
from productivity import ProductivitySystem

manager = Manager(id=1, name="John Smith", weekly_salary=1500)
secretary = Secretary(id=2, name="Rebeka Newman", weekly_salary=1200)
sales_guy = SalesPerson(id=3, name="Tom Jones", weekly_salary=1400, commission=350)
factory_worker = FactoryWorker(id=4, name="PetePeterson", hours_worked=40, hour_rate=15)

employees = [manager, secretary, sales_guy, factory_worker]

productivity_system = ProductivitySystem()
productivity_system.track(employees=employees, hours=40)

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees=employees)
