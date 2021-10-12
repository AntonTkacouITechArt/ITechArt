def analyze_students(data: dict) -> set:
    """get dict of student -> return set of tuple {(student, object name, multiple marks), ...} """
    return {tuple(
        [student_name, obj_name, functools.reduce(lambda x, y: x * y, marks)])
            for student_name, dtstudent in
            data.items() for obj_name, marks in dtstudent.items() if
            obj_name != '1C'}


def validate_data(data: dict) -> bool:
    """Validate data: check input student_name,object_name are str and are only english letters, also check marks are
    int type """
    for student_name, dt_student in data.items():

        if not isinstance(student_name, str):
            raise TypeError

        for obj_name, marks in dt_student.items():
            if not isinstance(obj_name, str):
                raise TypeError

            for el in marks:
                if not isinstance(el, int):
                    raise TypeError
                elif 1 <= el <= 10:
                    raise ValueError
                else:
                    pass

            if not obj_name.isalpha():
                raise ValueError

        if not student_name.isalpha():
            raise ValueError

    return True
