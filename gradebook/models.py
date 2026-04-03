class Student:
    def __init__(self, student_id: str, name: str):
        if not student_id or not isinstance(student_id, str):
            raise ValueError("student_id must be a non-empty string")
        if not name or not isinstance(name, str):
            raise ValueError("name must be a non-empty string")

        self.id = student_id
        self.name = name

    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"


class Course:
    def __init__(self, code: str, title: str):
        if not code or not isinstance(code, str):
            raise ValueError("code must be a non-empty string")
        if not title or not isinstance(title, str):
            raise ValueError("title must be a non-empty string")

        self.code = code
        self.title = title

    def __str__(self):
        return f"Course(code={self.code}, title={self.title})"


class Enrollment:
    def __init__(self, student_id: str, course_code: str, grades=None):
        if not student_id or not isinstance(student_id, str):
            raise ValueError("student_id must be a non-empty string")
        if not course_code or not isinstance(course_code, str):
            raise ValueError("course_code must be a non-empty string")

        if grades is None:
            grades = []

        if not isinstance(grades, list):
            raise ValueError("grades must be a list")

        for grade in grades:
            if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
                raise ValueError("each grade must be a number between 0 and 100")

        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades

    def __str__(self):
        return (
            f"Enrollment(student_id={self.student_id}, "
            f"course_code={self.course_code}, grades={self.grades})"
        )