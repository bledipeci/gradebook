import argparse
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa
)

from gradebook.logger import get_logger
logger = get_logger(__name__)

def parse_non_empty_string(value, field_name):
    if not value or not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value.strip()


def parse_grade(value):
    try:
        grade = float(value)
    except (TypeError, ValueError):
        raise ValueError("Grade must be a number")

    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100")

    return grade


def parse_id(value, field_name="ID"):
    if not value or not str(value).isdigit():
        raise ValueError(f"{field_name} must be a numeric string")
    return str(value)



def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    p_add_student = subparsers.add_parser("add-student")
    p_add_student.add_argument("--name", required=True)


    p_add_course = subparsers.add_parser("add-course")
    p_add_course.add_argument("--code", required=True)
    p_add_course.add_argument("--title", required=True)

    p_enroll = subparsers.add_parser("enroll")
    p_enroll.add_argument("--student-id", required=True)
    p_enroll.add_argument("--course", required=True)

    p_add_grade = subparsers.add_parser("add-grade")
    p_add_grade.add_argument("--student-id", required=True)
    p_add_grade.add_argument("--course", required=True)
    p_add_grade.add_argument("--grade", required=True)

    p_list = subparsers.add_parser("list")
    p_list.add_argument("type", choices=["students", "courses", "enrollments"])
    p_list.add_argument("--sort", choices=["name", "code"], required=False)

    p_avg = subparsers.add_parser("avg")
    p_avg.add_argument("--student-id", required=True)
    p_avg.add_argument("--course", required=True)

    p_gpa = subparsers.add_parser("gpa")
    p_gpa.add_argument("--student-id", required=True)

    args = parser.parse_args()

    try:

        if args.command == "add-student":
            name = parse_non_empty_string(args.name, "Name")
            student_id = add_student(name)
            print(f"Student added with ID: {student_id}")

        elif args.command == "add-course":
            code = parse_non_empty_string(args.code, "Course code")
            title = parse_non_empty_string(args.title, "Course title")
            add_course(code, title)
            print(f"Course '{code}' added")

        elif args.command == "enroll":
            student_id = parse_id(args.student_id, "Student ID")
            course_code = parse_non_empty_string(args.course, "Course code")
            enroll(student_id, course_code)
            print(f"Student {student_id} enrolled in {course_code}")

        elif args.command == "add-grade":
            student_id = parse_id(args.student_id, "Student ID")
            course_code = parse_non_empty_string(args.course, "Course code")
            grade = parse_grade(args.grade)
            add_grade(student_id, course_code, grade)
            print(f"Grade {grade} added")

        elif args.command == "list":
            if args.type == "students":
                students = list_students()
                if args.sort == "name":
                    students = sorted(students, key=lambda x: x["name"].lower())

                print("\nStudents:")
                for s in students:
                    print(f"{s['id']} - {s['name']}")

            elif args.type == "courses":
                courses = list_courses()
                if args.sort == "code":
                    courses = sorted(courses, key=lambda x: x["code"])

                print("\nCourses:")
                for c in courses:
                    print(f"{c['code']} - {c['title']}")

            elif args.type == "enrollments":
                enrollments = list_enrollments()

                print("\nEnrollments:")
                for e in enrollments:
                    print(f"{e['student_id']} | {e['course_code']} | {e['grades']}")

        elif args.command == "avg":
            student_id = parse_id(args.student_id, "Student ID")
            course_code = parse_non_empty_string(args.course, "Course code")

            avg = compute_average(student_id, course_code)
            if avg is None:
                print("No grades found or student not enrolled.")
            else:
                print(f"Average: {avg:.2f}")

        elif args.command == "gpa":
            student_id = parse_id(args.student_id, "Student ID")

            gpa = compute_gpa(student_id)
            if gpa is None:
                print("No grades available.")
            else:
                print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"Error: {e}")

    except Exception as e:
        logger.exception("Unexpected CLI error")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()