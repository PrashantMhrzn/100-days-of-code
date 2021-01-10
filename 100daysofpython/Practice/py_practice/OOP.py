class Employee:

    raise_per = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def raise_salary(self):
        self.salary = int(self.salary * self.raise_per)
        return self.salary

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


class Manager(Employee):
    raise_per = 1.10

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print('NO Employees Found!')

    @property
    def all_emp(self):
        for emp in self.employees:
            print(f'Name: {emp.fullname} Email: {emp.email}')
        return ''


class SeniorManager(Manager):
    raise_per = 1.50

    def __init__(self, first, last, salary, employees=None, manager=None):
        super().__init__(first, last, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

        if manager == None:
            self.manager = []
        else:
            self.manager = manager

    def add_managers(self, manager):
        if manager not in self.manager:
            self.manager.append(manager)

    def remove_managers(self, manager):
        if manager in self.manager and isinstance(manager, Manager):
            self.manager.remove(manager)
        else:
            print('No Manager Found!')

    @property
    def all_managers(self):
        for manager in self.manager:
            print(f'Name: {manager.fullname} Email: {manager.email}')
        return ''
