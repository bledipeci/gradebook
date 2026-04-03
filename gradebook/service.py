from .models import Student, Course, Enrollment
from .storage import load_data, save_data


def _get_data():
    """Load and normalize gradebook data structure."""
    data = load_data()
    return {
        "students": data.get("students", []),
        "courses": data.get("courses", []),
        "enrollments": data.get("enrollments", []),
    }


def _save(data):
    """Persist data to storage."""
    save_data(data)


def _generate_student_id(students):
    """Generate a simple incremental student ID."""
    return str(len(students) + 1)


def add_student(name):
    """
    Add a new student.

    Args:
        name (str): Student name.

    Returns:
        str: Generated student ID.
    """
    data = _get_data()
    student_id = _generate_student_id(data["students"])

    student = Student(student_id, name)
    data["students"].append(student.__dict__)

    _save(data)
    return student_id


def add_course(code, title):
    """
    Add a new course.

    Args:
        code (str): Course code.
        title (str): Course title.

    Raises:
        ValueError: If course already exists.
    """
    data = _get_data()

    if any(c["code"] == code for c in data["courses"]):
        raise ValueError("Course already exists")

    course = Course(code, title)
    data["courses"].append(course.__dict__)

    _save(data)


def enroll(student_id, course_code):
    """
    Enroll a student in a course.

    Raises:
        ValueError: If student/course not found or already enrolled.
    """
    data = _get_data()

    if not any(s["id"] == student_id for s in data["students"]):
        raise ValueError("Student not found")

    if not any(c["code"] == course_code for c in data["courses"]):
        raise ValueError("Course not found")

    if any(
        e["student_id"] == student_id and e["course_code"] == course_code
        for e in data["enrollments"]
    ):
        raise ValueError("Already enrolled")

    enrollment = Enrollment(student_id, course_code)
    data["enrollments"].append(enrollment.__dict__)

    _save(data)


def add_grade(student_id, course_code, grade):
    """
    Add a grade to a student's enrollment.

    Raises:
        ValueError: If enrollment not found or grade invalid.
    """
    if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100")

    data = _get_data()

    enrollment = next(
        (
            e
            for e in data["enrollments"]
            if e["student_id"] == student_id
            and e["course_code"] == course_code
        ),
        None,
    )

    if not enrollment:
        raise ValueError("Enrollment not found")

    enrollment["grades"].append(grade)
    _save(data)


def list_students():
    """
    List all students sorted by name.

    Returns:
        list[dict]: Students.
    """
    data = _get_data()

    return sorted(
        [{"id": s["id"], "name": s["name"]} for s in data["students"]],
        key=lambda x: x["name"].lower(),
    )


def list_courses():
    """
    List all courses sorted by code.

    Returns:
        list[dict]: Courses.
    """
    data = _get_data()

    return sorted(
        [{"code": c["code"], "title": c["title"]} for c in data["courses"]],
        key=lambda x: x["code"],
    )


def list_enrollments():
    """
    List all enrollments sorted by student and course.

    Returns:
        list[dict]: Enrollments.
    """
    data = _get_data()

    return sorted(
        [
            {
                "student_id": e["student_id"],
                "course_code": e["course_code"],
                "grades": e["grades"],
            }
            for e in data["enrollments"]
        ],
        key=lambda x: (x["student_id"], x["course_code"]),
    )


def compute_average(student_id, course_code):
    """
    Compute average grade for a course.

    Returns:
        float | None: Average or None if no grades.
    """
    data = _get_data()

    grades = next(
        (
            e["grades"]
            for e in data["enrollments"]
            if e["student_id"] == student_id
            and e["course_code"] == course_code
        ),
        [],
    )

    return sum(grades) / len(grades) if grades else None


def compute_gpa(student_id):
    """
    Compute GPA (mean of course averages).

    Returns:
        float | None: GPA or None if no data.
    """
    data = _get_data()

    averages = [
        sum(e["grades"]) / len(e["grades"])
        for e in data["enrollments"]
        if e["student_id"] == student_id and e["grades"]
    ]

    return sum(averages) / len(averages) if averages else None