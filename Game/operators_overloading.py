
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        marks1 = self.m1 + other.m1
        marks2 = self.m2 + other.m2
        adding = Student(marks1, marks2)
        return adding

    def __gt__(self, other):
        total1 = self.m1 + self.m2
        total2 = other.m1 + other.m2
        if total1 > total2:
            return True
        else:
            return False


s1 = Student(10, 50)
s2 = Student(30, 70)

s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
