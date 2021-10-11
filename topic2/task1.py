import typing


class Department:
    class BudgetError(ValueError):
        """Budget below zero"""

    def __init__(self, name: typing.Optional[str],
                 employees: typing.Dict[str, float],
                 budget: typing.Optional[int]):
        self.budget = budget
        self.employees = employees
        self.name = name

    def __str__(self):
        # return f"""{self.name} ({len(self.employees)} - {self.average_salary}, {self.budget})"""
        return '{} ({} - {}, {})'.format(self.name, len(self.employees),
                                         self.average_salary, self.budget)

    def __or__(self, other: 'Department') -> 'Department':
        a = self.get_budget_plan
        b = other.get_budget_plan
        if a > 0 and b > 0:
            if a >= b:
                return self
            else:
                return other
        raise Department.BudgetError("""One of the company 
        has a negative budget""")

    def __add__(self, other: 'Department') -> 'Department':
        budget = self.budget + other.budget
        employees = {}
        employees.update(self.employees)
        employees.update(other.employees)
        if self.average_salary > other.average_salary:
            name = self.name + ' - ' + other.name
        elif self.average_salary == other.average_salary:
            if self.name >= other.name:
                name = self.name + ' - ' + other.name
            else:
                name = other.name + ' - ' + self.name
        else:
            name = other.name + ' - ' + self.name
        temp = Department(name, employees, budget)
        _ = temp.get_budget_plan
        return temp

    @property
    def get_budget_plan(self) -> float:
        all_salary = sum(self.employees.values())
        department_budget = float(self.budget) - all_salary
        if department_budget < 0:
            raise Department.BudgetError("""the depatment 
            has a negative budget""")
        return department_budget

    @property
    def average_salary(self) -> float:
        avg_salary = sum(self.employees.values()) / len(self.employees)
        avg_salary = avg_salary - avg_salary % 0.01
        return avg_salary

    @classmethod
    def merge_departments(cls, *departments: 'Department') -> 'Department':
        all_budget = 0
        name = ''
        employees = {}
        sorted_list = []
        for department in departments:
            all_budget += department.budget
            employees.update(department.employees)
            sorted_list.append(tuple([department.average_salary,department.name]))

        # a = sorted_list.sort(key=lambda i: i[0], reverse=True)
        sorted_list = sorted(sorted_list, key=lambda i: i[0], reverse=True)
        sorted_list = sorted(sorted_list, key=lambda i: i[1])
        for other_name in sorted_list:
            name += other_name[1]
            if sorted_list[-1][1] != other_name[1]:
                name += ' - '
        temp = Department(name, employees, all_budget)
        return temp


if __name__ == '__main__':
    data = {
        'AntonT': 400.0,
        'Valeria': 400.0,
        'Vlad': 1000.0,
        'AntonL': 1500.0,
        'Pavel': 3000.0,
    }
    data1 = {
        'AntonT1': 4500.0,
        'Valeria1': 400.0,
        'Vlad1': 1000.0,
        'AntonL1': 1500.0,
        'Pavel1': 3000.0,
    }
    data2 = {
        'Steve': 1000.0,
        'Peter': 400.0,
        'Gramm': 1000.0,
        'Andersen': 1500.0,
        'Paul': 3000.0,
    }

    dep1 = Department("ITeach", data, 10000)
    dep2 = Department("ITeac", data, 12000)
    dep3 = Department("ITeach2", data1, 12000)
    dep4 = Department("AnderLow", data2, 20000)
    # print(f"Budget department: {dep1.get_budget_plan}")
    # # dep3 = Department.merge_departments(dep1, dep2)
    # a = dep1 + dep2
    # print(a)

    dep_test = Department.merge_departments(dep1, dep2, dep4)
    print(dep_test.name)
