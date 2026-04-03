# Gradebook CLI App

A simple Python-based gradebook system with CLI support.
It allows you to manage students, courses, enrollments, and grades, and compute averages and GPA.

---

## Features

* Add students and courses
* Enroll students in courses
* Add grades (0–100)
* Compute course averages and GPA
* Persistent storage using JSON
* CLI interface using argparse
* Logging to file
* Unit tests included

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd gradebook
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **macOS/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

No external dependencies required (standard library only).

---

## Seed Sample Data

Populate the app with sample data:

```bash
python scripts/seed.py
```

This will create:

* 3 students
* 2 courses
* enrollments
* several grades

Data is saved to:

```
data/gradebook.json
```

---

## CLI Usage

Run commands using:

```bash
python main.py <command> [options]
```

---

### Add a student

```bash
python main.py add-student --name "Bledi"
```

**Output:**

```
Student added with ID: 1
```

---

### Add a course

```bash
python main.py add-course --code CS101 --title "Intro to CS"
```

---

### Enroll a student

```bash
python main.py enroll --student-id 1 --course CS101
```

---

### Add a grade

```bash
python main.py add-grade --student-id 1 --course CS101 --grade 95
```

---

### List data

```bash
python main.py list students
python main.py list courses
python main.py list enrollments
```

---

### Compute average

```bash
python main.py avg --student-id 1 --course CS101
```

**Output:**

```
Average: 92.50
```

---

### Compute GPA

```bash
python main.py gpa --student-id 1
```

---

## Run Tests

```bash
python -m unittest discover tests
```

---

## Project Structure

```
gradebook/
│
├── main.py
├── data/
├── logs/
├── scripts/
│   └── seed.py
├── tests/
│   └── test_service.py
│
└── gradebook/
    ├── __init__.py
    ├── models.py
    ├── service.py
    ├── storage.py
    └── logger.py
```

---

### Design Decisions

* **Layered architecture**

  * `models.py` → data structures + validation
  * `service.py` → business logic
  * `storage.py` → persistence
  * `main.py` → CLI interface

* **JSON storage**

  * Simple and human-readable
  * No external database required

* **Pure-like service functions**

  * Encapsulate logic cleanly
  * Easy to test and reuse

* **Validation layer in CLI**

  * Prevents bad input before reaching logic

* **Logging**

  * Errors and actions written to `logs/app.log`

---

## Author

Bledi Peci
