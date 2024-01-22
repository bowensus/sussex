class Student:
    """A class to represent a University student."""
    def __init__(self, first, last, course):
        self.first = first
        self.last = last
        self.course = course
        self.module_number = []

    def show_details(self):
        print("{:s} {:s} on course: {:s}". format(self.first, self.last, self.course))
        print("Enrolled on following modules:")
        for x in self.module_number:
            print(x)

    def change_course(self, changed):
        self.course = changed
        
class Module:
    """A class to represent a single module."""
    def __init__(self, name, number, lecturer):
        self.name = name
        self.number = number
        self.lecturer = lecturer
        self.stu_list = []

    def enrol_student(self, student):
        self.stu_list.append(student.first + " " + student.last)
        student.module_number.append(self.number)

    def show_all_enrolled_students(self):
        if len(self.stu_list) != 0:
            print("Enrolled on module: {:s}". format(self.number))
            for x in self.stu_list:
                print(x)
        else:
            print("No students for {:s} yet". format(self.number))

def main():

    # Create some students and some modules...
    s1 = Student('Ken', 'Barlow', 'English')
    s2 = Student('Mike', 'Baldwin', 'Business')
    s3 = Student('Harold', 'Legg', 'Medicine')

    m1 = Module('English language and semantics', 'A101', 'Wanda Pickle')
    m2 = Module('Engineering principles', 'E102', 'Buzz Jones')
    m3 = Module('Anatomy', 'M105', 'Greg House')

    # Now enrol some students on some modules...
    m1.enrol_student(s1)
    m1.enrol_student(s2)
    m2.enrol_student(s1)
    m2.enrol_student(s3)

    # Have a look at some students and some modules...
    s1.show_details()
    s2.show_details()
    s3.show_details()

    m1.show_all_enrolled_students()
    m2.show_all_enrolled_students()
    m3.show_all_enrolled_students()

    # Change a course...
    s1.change_course('Engineering')
    s1.show_details()


if __name__ == "__main__":
    main()
