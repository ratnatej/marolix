#create a class school,create at least 5 attributes,call those attributeusing at least 10 object
class School:
    def __init__(self, school_name, location, student_name, marks_students, subjects):
        self.school_name = school_name
        self.location = location
        self.student_name = student_name
        self.marks_students = marks_students
        self.subjects = subjects

school1 = School("Narayana School", "Tenali", "Mr. student1", 500, "maths")
school2 = School("Chaithanya School", "Tenali", "Ms. student2", 300, "pyhs")
school3 = School("Ratna School", "Tenali", "Mr. student3", 400, "che")
school4 = School("Teja School", "Tenali", "Mrs. student4", 350, "m1")
school5 = School("Deppu School", "Tenali", "Mr. student5", 450, "edc")
school6 = School("Anu School", "Tenali", "Ms. student6", 250, "social")
school7 = School("Vamsi School", "Tenali", "Mr. student7", 600, "coms")
school8 = School("John School", "Tenali", "Ms. student8", 550, "ews")
school9 = School("Vem School", "Tenali", "Mr. student9", 400, "m2")
school10 = School("Swathi School", "Tenali", "Mrs. student10", 350, "m3")

print(school1.school_name)
print(school2.location)
print(school3.student_name)
print(school4.marks_students)
print(school5.subjects)
print(school6.school_name)
print(school7.location)
print(school8.student_name)
print(school9.marks_students)
print(school10.subjects)
