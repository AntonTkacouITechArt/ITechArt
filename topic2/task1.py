class Department:
    class BudgetError(ValueError):
        """Budget below zero"""

    def __init__(self, name: typing.Optional[str],
                 employees: typing.Dict[str, float], budget: typing.Optional[int]):
        self.budget = budget
        self.employees = employees
        self.name = name

    def __str__(self):
        return f"""{self.name} ({len(self.employees)} - 
        {self.average_salary()}, {self.budget})"""

    # add type hint references on close class
    def __or__(self, other: 'Department') -> 'Department':
        a = self.get_budget_plan()
        b = other.get_budget_plan()
        if a > 0 and b > 0:
            if a >= b:
                return self
            else:
                return other
        raise Department.BudgetError("""One of the company 
        has a negative budget""")

    # говно код???
    def __add__(self, other: 'Department') -> 'Department':
        budget = self.budget + other.budget
        name = self.name + ' - ' + other.name
        employees = {}
        employees.update(self.employees)
        employees.update(other.employees)
        return Department(name, employees, budget)

    def get_budget_plan(self) -> float:
        department_budget = float(self.budget)
        for name_emp, salary in self.employees.items():
            department_budget -= salary
        if department_budget < 0:
            raise Department.BudgetError("""the depatment 
            has a negative budget""")
        return department_budget

    def average_salary(self) -> float:
        avg_salary = 0.0
        for name_emp, salary in self.employees.items():
            avg_salary += salary
        avg_salary /= len(self.employees)
        avg_salary = avg_salary - avg_salary % 0.01
        return avg_salary

    def merge_departments(self):
        pass


    # add type hint references on close class
    # говно код
    # def get_budget_key(obj):
    #     return obj.average_salary()

    # @classmethod
    # def merge_departments(cls, *departments):
    #     departments = list(departments)
    #     departments1 = departments.sort(key=cls.get_budget_key, reverse=True)
    #     print(departments)
    #     budget = 0
    #     employees = dict()
    #     name = ''
    #
    #     for department in departments:
    #         employees.update(department)
    #         name += ''
    #         budget += department.budget
    #     return Department()


# if __name__ == '__main__':
#     data = {
#         'AntonT': 400.0,
#         'Valeria': 400.0,
#         'Vlad': 1000.0,
#         'AntonL': 1500.0,
#         'Pavel': 3000.0,
#     }
#     data1 = {
#         'AntonT1': 4500.0,
#         'Valeria1': 400.0,
#         'Vlad1': 1000.0,
#         'AntonL1': 1500.0,
#         'Pavel1': 3000.0,
#     }
#
#     dep1 = Department("ITeach", data, 10000)
#     dep2 = Department("ITeach1", data1, 12000)
#     dep3 = Department("ITeach2", data1, 12000)
#
#     print(f"Budget department: {dep1.get_budget_plan()}")
#     # dep3 = Department.merge_departments(dep1, dep2)
#     a = dep1 + dep2
#     print(a)
