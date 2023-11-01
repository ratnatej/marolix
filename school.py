#create a class school,create at least 5 attributes,call those attributeusing at least 10 object
class School:
    def __init__(self, school_name, location, student_name, marks_students, teacher_name):
        self.school_name = school_name
        self.location = location
        self.student_name = student_name
        self.marks_students = marks_students
        self.teacher_name = teacher_name

school1 = School("Narayana School", "Tenali", "Mr. student1", 500, "rajesh")
school2 = School("Chaithanya School", "Tenali", "Ms. student2", 300, "Sneha")
school3 = School("Ratna School", "Tenali", "Mr. student3", 400, "sudha")
school4 = School("Teja School", "Tenali", "Mrs. student4", 350, "Manoj")
school5 = School("Deppu School", "Tenali", "Mr. student5", 450, "Anita")
school6 = School("Anu School", "Tenali", "Ms. student6", 250, "rakesh")
school7 = School("Vamsi School", "Tenali", "Mr. student7", 600, "ramesh")
school8 = School("John School", "Tenali", "Ms. student8", 550, "ramu")
school9 = School("Vem School", "Tenali", "Mr. student9", 400, "tej")
school10 = School("Swathi School", "Tenali", "Mrs. student10", 350, "lex")

print(school1.school_name)
print(school2.location)
print(school3.student_name)
print(school4.marks_students)
print(school5.teacher_name)
print(school6.school_name)
print(school7.location)
print(school8.student_name)
print(school9.marks_students)
print(school10.teacher_name)
