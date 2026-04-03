import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
)
from gradebook.storage import DEFAULT_PATH


def seed_data():
    """Populate the gradebook with sample data."""


    if os.path.exists(DEFAULT_PATH):
        os.remove(DEFAULT_PATH)

    print("Seeding sample data...\n")


    s1 = add_student("Bledi Peci")
    s2 = add_student("Arta Krasniqi")
    s3 = add_student("Luan Gashi")

    print(f"Added students: {s1}, {s2}, {s3}")


    add_course("CS101", "Intro to Computer Science")
    add_course("MATH201", "Discrete Mathematics")

    print("Added courses: CS101, MATH201")


    enroll(s1, "CS101")
    enroll(s1, "MATH201")

    enroll(s2, "CS101")
    enroll(s3, "MATH201")

    print("Enrollments created")

  
    add_grade(s1, "CS101", 90)
    add_grade(s1, "CS101", 85)

    add_grade(s1, "MATH201", 88)

    add_grade(s2, "CS101", 76)
    add_grade(s2, "CS101", 82)

    add_grade(s3, "MATH201", 95)

    print("Grades added")

    print("\n Seeding complete!")
    print(f"Data saved to: {DEFAULT_PATH}")


if __name__ == "__main__":
    seed_data()