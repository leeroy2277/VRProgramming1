class Student:

    def __init__(self, id, name, gpa):

        self.id = id
        self.name = name
        self.gpa = gpa


class StudentClass:

    def __init__(self):

        self.__student_list = []

    def add_student(self, student: Student):

        self.__student_list.append(student)

    def remove_student(self, student_id):

        for current_student in self.__student_list:

            if current_student.id == student_id:

                self.__student_list.remove(current_student)

    def list_students(self):

        for student in self.__student_list:
            print ("Student ID: " + str(student.id) + " Student Name: " + student.name)

    def get_count_of_students(self):

        return len(self.__student_list)


    def get_avg_gpa(self):

        gpa_total = 0

        for student in self.__student_list:
            gpa_total += student.gpa


        return gpa_total / self.get_count_of_students()









math_101 = StudentClass()



s1 = Student(100, "Mary", 4)
s2 = Student(200, "Bob", 4)
s3 = Student(300, "Brendan", 4)

math_101.add_student(s1)
math_101.add_student(s2)
math_101.add_student(s3)
#math_101.remove_student(200)

math_101.list_students()

print("The number of students left in this class is " + str(math_101.get_count_of_students()))

print( str(math_101.get_avg_gpa()))
