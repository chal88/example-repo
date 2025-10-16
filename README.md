OOP Course Management - Python Example

This Python program demonstrates the fundamentals of **Object-Oriented Programming (OOP)** using a simple course management system.

The script defines a base class `Course` and a subclass `OOPCourse`, showcasing concepts such as inheritance, method overriding, class and instance attributes, and object instantiation.

Features

`Course` Class (Parent Class)

Represents a generic course offering.

**Attributes:**
- `name` – Name of the course (`"Fundamentals of Computer Science"`)
- `contact_website` – Website for contacting the course provider (`"www.hyperiondev.com"`)
- `location` – Head office location (`"Cape Town"`)

**Methods:**
- `contact_details()` – Prints the course provider's contact website.
- `head_office_loc()` – Prints the location of the head office.

---

`OOPCourse` Class (Subclass of `Course`)

A specific course focused on **Object-Oriented Programming**.

**Constructor Parameters (with default values):**
- `description = "OOP Fundamentals"` – Describes the course content.
- `trainer = "Mr. Anon A. Mouse"` – Name of the course trainer.

**Methods:**
- `trainer_details()` – Prints the course description and the trainer's name.
- `show_course_id()` – Prints a hardcoded course ID (`#12345`).

---

Example Usage

The following object is created and class methods are called:

```python
# Create an instance of OOPCourse
course_1 = OOPCourse()

# Call inherited and subclass-specific methods
course_1.contact_details()     # Inherited from Course
course_1.trainer_details()     # Defined in OOPCourse
course_1.show_course_id()      # Defined in OOPCourse

# Create an instance of the base class
course = Course()
course.head_office_loc()       # Method from Course class
