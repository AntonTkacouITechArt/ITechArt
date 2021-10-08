# from typing import Optional, Dict
#
#
# class Department:
#     class BudgetError(ValueError):
#         """The department doesn't have budget to cover salary """
#
#     def __init__(self, name: Optional[str], employees: Dict[str, float], budget: Optional[int]):
#         self.budget = budget
#         self.employees = employees
#         self.name = name
#
#     def get_budget_plan(self) -> float:
#         department_budget = float(self.budget)
#         for name_emp, salary in self.employees.items():
#             department_budget -= salary
#         if department_budget < 0:
#             raise Department.BudgetError("""The department doesn't have budget to cover salary """)
#         return department_budget
#
#
# if __name__ == '__main__':
#     data = {
#         'AntonT': 400.0,
#         'Valeria': 400.0,
#         'Vlad': 1000.0,
#         'AntonL': 1500.0,
#         'Pavel': 3000.0,
#     }
#
#     dep1 = Department("ITeach", data, 10000)
#     print(f"Budget department: {dep1.get_budget_plan()}")
