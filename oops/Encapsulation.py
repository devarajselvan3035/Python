from ast import Constant


def average(num_list: list) -> float:
    total = 0.0
    for num in num_list:
        total += num
    len_num = len(num_list)
    return total / len_num


class Person:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        self.constant = 10


# oPerson1 = Person("Joe Schmoe", 90000)
# oPerson2 = Person("Jane Smith", 99000)
#
# # Get the values of the salary variable directly
# print(oPerson1.salary)
# print(oPerson2.salary)
#
# # Change the salary variable directly
# oPerson1.salary = 100000
# oPerson2.salary = 111111
#
# # Get the updated salaries and print again
# print(oPerson1.salary)
# print(oPerson2.salary)
#
class Example:
    def __init__(self, x) -> None:
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 10:
            self._x = value


exam = Example(10)
print(exam.x, exam._x)
exam.x = 20
print(exam.x, exam._x)
