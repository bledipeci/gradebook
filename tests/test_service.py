import unittest
import os
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    compute_average
)
from gradebook.storage import DEFAULT_PATH


class TestService(unittest.TestCase):
    """Unit tests for gradebook service layer."""

    def setUp(self):
        """Reset test data before each test."""
        if os.path.exists(DEFAULT_PATH):
            os.remove(DEFAULT_PATH)

    def test_add_student(self):
        """Test adding a student returns a valid ID."""
        student_id = add_student("Bledi")

        self.assertIsNotNone(student_id)
        self.assertEqual(student_id, "1")

    def test_add_grade_and_compute_average(self):
        """Test adding grades and computing average."""
        student_id = add_student("Bledi")
        add_course("CS101", "Intro to CS")
        enroll(student_id, "CS101")

        add_grade(student_id, "CS101", 90)
        add_grade(student_id, "CS101", 100)

        avg = compute_average(student_id, "CS101")

        self.assertEqual(avg, 95)

    def test_compute_average_no_grades(self):
        """Edge case: no grades should return None."""
        student_id = add_student("Bledi")
        add_course("CS101", "Intro to CS")
        enroll(student_id, "CS101")

        avg = compute_average(student_id, "CS101")

        self.assertIsNone(avg)

    def test_add_grade_invalid(self):
        """Failing case: invalid grade should raise ValueError."""
        student_id = add_student("Bledi")
        add_course("CS101", "Intro to CS")
        enroll(student_id, "CS101")

        with self.assertRaises(ValueError):
            add_grade(student_id, "CS101", 150)

if __name__ == "__main__":
    unittest.main()