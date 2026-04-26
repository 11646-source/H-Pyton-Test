#!/usr/bin/env python3

from school_management import Person


class Student(Person):
    def __init__(self, name, age, student_id, course_list):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = course_list

    def __str__(self):
        return "{} ({}) - ID: {} - Courses: {}".format(
            self.name,
            self.age,
            self.student_id,
            ", ".join(self.course_list)
        )
