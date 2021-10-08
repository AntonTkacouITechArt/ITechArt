def analyze_students(data: dict) -> set:
    """get dict of student -> return set of tuple {(student, object name, multiple marks), ...} """
    return {tuple([student_name, obj_name, functools.reduce(lambda x, y: x * y, marks)]) for student_name, dtstudent in
            data.items() for obj_name, marks in dtstudent.items() if obj_name != '1C'}


def validate_data(data: dict) -> bool:
    """Validate data: check input student_name,object_name are str and are only english letters, also check marks are
    int type """
    for student_name, dt_student in data.items():

        if type(student_name) is not str:
            raise TypeError

        for obj_name, marks in dt_student.items():
            if obj_name is not str:
                raise TypeError

            for el in marks:
                if el is not int:
                    raise TypeError
                elif el < 1 or el > 10:
                    raise ValueError
                else:
                    pass

            for letter in obj_name:
                if ord(letter) < 65 or ord(letter) > 122:
                    raise ValueError

        for letter in student_name:
            if ord(letter) < 65 or ord(letter) > 122:
                raise ValueError
    return True
