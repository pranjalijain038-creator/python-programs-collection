from dataclasses import dataclass, asdict


@dataclass
class Student:
    name: str
    age: int
    course: str


student = Student(
    name="Pranjali",
    age=20,
    course="B.Tech CSE"
)

student_dictionary = asdict(student)

print("Student Dictionary:")
print(student_dictionary)

