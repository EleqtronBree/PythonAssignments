"""
Author: Electra Bree
Assignment related to classes
"""

# Question 1
# Manages student results in a course
class Student:
    
    def __init__(self, first_name, surname, student_id, email_address):
        self.__first_name = first_name
        self.__surname = surname
        self.__student_id = student_id
        self.__email_address = email_address
        self.__test_mark = 0
        self.__exam_mark = 0
        self.__lab_marks = []
        
    def __str__(self):
        return "{}, {}: id={} ({})".format(self.__surname.title(), self.__first_name.title(), self.__student_id, self.__email_address)

    def set_test_mark(self, mark):
        if mark >= 0 and mark <= 100:
            self.__test_mark = mark
            
    def get_test_mark(self):
        return self.__test_mark
        
    def set_exam_mark(self, mark):
        if mark >= 0 and mark <= 100:
            self.__exam_mark = mark
            
    def get_exam_mark(self):
        return self.__exam_mark
        
    def add_lab_mark(self, mark):
        if mark >= 0 and mark <= 100:
            self.__lab_marks += [mark]
            
    def get_lab_marks(self):
        return self.__lab_marks
    
    def get_average_lab_mark(self):
        if len(self.__lab_marks) > 0:
            total = 0
            for mark in self.__lab_marks:
                total += mark
            return round(total / len(self.__lab_marks), 1)
        else:
            return 0
    
    def get_final_mark(self):
        lab_marks = 0 
        if len(self.__lab_marks) > 0:
            for mark in self.__lab_marks:
                lab_marks += mark
        lab_marks *= 0.1
        test_mark = self.__test_mark * 0.2
        exam_marks = self.__exam_mark * 0.4
        return lab_marks + test_mark + exam_marks
        
    def get_grade(self):
        final_mark = self.get_final_mark()
        grade = "F"
        if final_mark >= 90 and final_mark <= 100:
            grade = "A"
        elif final_mark >= 75:
            grade = "B"
        elif final_mark >= 50:
            grade = "C"
        elif final_mark >= 40:
            grade = "D"
        elif final_mark >= 30:
            grade = "E"
        return grade

# Question 2
# Represents a simple polynomial with a degree of 3
class SimplePolynomial:
    
    def __init__(self, a = 1, b = 1, c = 1):
        self.__coefficients = [a, b, c]
        
    def __str__(self):
        a = self.__coefficients[0]
        b = self.__coefficients[1]
        c = self.__coefficients[2]
        if a != 0 and b != 0 and c != 0:
            return "{}x^2 + {}x + {}".format(c, b, a)
        elif a != 0 and b != 0:
            return "{}x + {}".format(b, a)
        elif a != 0 and c != 0:
            return "{}x^2 + {}".format(c, a)
        elif b != 0 and c != 0:
            return "{}x^2 + {}x".format(c, b)
        elif c != 0:
            return "{}x^2".format(c)
        elif b != 0:
            return "{}x".format(b)
        else:
            return "{}".format(a)
    
    def evaluate(self, x):
        a = self.__coefficients[0]
        b = self.__coefficients[1]
        c = self.__coefficients[2]
        return c*x**2 + b*x + a
        
    def __add__(self, x):
        self_a = self.__coefficients[0]
        self_b = self.__coefficients[1]
        self_c = self.__coefficients[2]
        x_a = x.__coefficients[0]
        x_b = x.__coefficients[1]
        x_c = x.__coefficients[2]
        
        a = self_a + x_a
        b = self_b + x_b
        c = self_c + x_c
        
        return SimplePolynomial(a,b,c)
