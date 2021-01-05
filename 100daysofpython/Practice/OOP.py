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
        if manager in self.manager and isinstance(manager,Manager):
            self.manager.remove(manager)
        else:
            print('No Manager Found!')
    
    @property
    def all_managers(self):
        for manager in self.manager:
            print(f'Name: {manager.fullname} Email: {manager.email}')
        return ''


emp1 = Employee('Arya', 'Stark', 50000)
emp2 = Employee('Ricon', 'Stark', 55000)
emp3 = Employee('Bran', 'Stark', 60000)
emp4 = Employee('John', 'Snow', 100000)
j_manage1 = Manager('Sanasa', 'Stark', 500000)
j_manage2 = Manager('Robb', 'Stark', 300000)
s_manage2 = SeniorManager('Edard', 'Stark', 1000000)

# print(help(SeniorManager))

print('***Employee Class Functionality***')
print(emp1.first)
print(emp1.last)
print(f'Before raise ${emp1.salary}')
emp1.raise_salary()
print(f'After raise ${emp1.salary}')
print(emp1.fullname)
print(emp1.email)

print('\n\n***Manager Class Functionality***')
print(j_manage1.first)
print(j_manage1.last)
print(f'Before raise ${j_manage1.salary}')
j_manage1.raise_salary()
print(f'After raise ${j_manage1.salary}')
print(j_manage1.fullname)
print(j_manage1.email)
j_manage1.add_emp(emp1)
j_manage1.add_emp(emp2)
j_manage1.remove_emp(emp1)
print(f'Added Employees: {j_manage1.all_emp}')

print('\n\n***Senoir Manager Class Functionality***')
print(s_manage2.first)
print(s_manage2.last)
print(f'Before raise ${s_manage2.salary}')
s_manage2.raise_salary()
print(f'After raise ${s_manage2.salary}')
print(s_manage2.fullname)
print(s_manage2.email)
s_manage2.add_emp(emp3)
s_manage2.add_emp(emp4)
s_manage2.remove_emp(emp3)
print(f'Added Employees: {s_manage2.all_emp}')
s_manage2.add_managers(j_manage1)
s_manage2.add_managers(j_manage2)
s_manage2.remove_managers(j_manage1)
print(f'Added Managers: {s_manage2.all_managers}')