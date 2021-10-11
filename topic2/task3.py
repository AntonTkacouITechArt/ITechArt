import dataclasses
import typing


@dataclasses.dataclass(order=True)
class Student:
    name: str = dataclasses.field(repr=True, compare=False)
    first_letter: str = dataclasses.field(init=False,
                                          repr=False,
                                          compare=False)
    average_mark: float = dataclasses.field(compare=True,
                                            repr=True)
    age: int = dataclasses.field(default=18, repr=False,
                                 compare=False)
    subjects: typing.List[str] = dataclasses.field(default_factory=list,
                                                   repr=False,
                                                   compare=False)

    def __post_init__(self):
        if self.name == '':
            self.first_letter = None
        else:
            self.first_letter = self.name[0]


if __name__ == '__main__':
    a = Student(name='Anton', average_mark=8.5, age=19, subjects=['en', 'rus'])
    b = Student(name='Sasha', average_mark=9, age=18, subjects=['math', 'phis'])
    c = Student(name='', average_mark=7, age=19, subjects=['math', 'phis'])
    d = [b, c, a]
    print(d)
    print(sorted(d))
    print(a)
    print(repr(a))
    print(a.first_letter)
    print(b.first_letter)
    print(c.first_letter)
    print(a.name)
    print(a.age)
    print(a.subjects)
    print(a < b)
    print(a > c)
