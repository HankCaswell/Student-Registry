import re

class Student:
    counter = 0
    def __init__(self, name, age =13, grade= "12th"):
        self._name = name
        self._age = age
        self._grade = grade
        Student.counter += 1 
        self.student_counter = Student.counter
        
    @property
    def get_name(self):
        return self._name
    @get_name.setter #Ask about how to get to the false return statement
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 3 and new_name.istitle() and new_name.isalnum():
            self._name = new_name
        else: 
            print("Name must be a string, 3 characters or more, hold no spaces or special characters, and be in title format")
    @property
    def get_age(self):
        return self._age
    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int and 11<new_age and 18>new_age:
            self._age = new_age
        else:
            print("Age must be an integer between 11 and 18.")
    @property
    def get_grade(self):
        return self._grade
    @get_grade.setter
    def set_grade(self, new_grade):
        grade_list = ["9th", "10th", "11th", "12th"]
        if new_grade in grade_list:
            self._grade = new_grade
        else: 
            print("Student must be in 9th-12th Grade.")
    def __str__(self):
        return f"Student {self.student_counter} Name : {self._name}, Age: {self._age}, Grade: {self._grade}"
    def advance(self, years_advanced):
        grade_list = ["9th", "10th", "11th", "12th", "13th"]
        self._grade = grade_list[grade_list.index(self._grade) + years_advanced]
    def study(self, subject):
        return f'{self._name} is studying {subject}'

      
      
      


student_1 = Student("Francisco", 15, "12th")
student_2 = Student("Alice")
student_3 = Student('Bob')
print(student_1)
print(student_2)
print(student_3)
# student_1.set_age = 16
# student_1.set_name = "Michael"
# student_1.set_grade = "11th"
# student_1.advance(1)
# student_1.study("Biology")



# print(student_1.get_age)
# print(student_1.get_name)
# print(student_1.get_grade)

