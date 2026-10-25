
# Convert a structure-like record into a dictionary

from dataclasses import dataclass, asdict


@dataclass
class Student:
    name: str
    age: int
    branch: str


student = Student(
    name=input("Enter student name: "),
    age=int(input("Enter student age: ")),
    branch=input("Enter student branch: ")
)

student_dict = asdict(student)

print("Student Dictionary:")
print(student_dict)
