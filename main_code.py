import copy
import json
from colorama import Fore, Back, Style
class Course:
    """
    Represents a course with its ID, name, units, and score.
    """
    id: int = 0
    name: str = ""
    units: int = 0
    score: int = 0
    def __init__(self, id, name, units, score):
        """
        Initialize a Course object.

        Args:
            id (int): The unique ID of the course.
            name (str): The name of the course.
            units (int): The number of course units.
            score (int): The student's score in the course.
        """
        self.id = id
        self.name = name
        self.units = units
        self.score = score
    def __eq__(self, other):
        """
        Compare the course with another Course object or an integer ID.

        Args:
            other (Course or int): The object or course ID to compare with.

        Returns:
            bool: True if the course IDs are equal, otherwise False.
        """
        if isinstance(other, Course):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
    def __str__(self):
        """
        Return a formatted string containing the course information.

        Returns:
            str: The course ID, name, units, and score.
        """
        return f"{self.id}\t{self.name}\t{self.units}\t{self.score} "
class Student:
    """
    Represents a student with an ID, name, family name, and courses.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course] = []
    def __init__(self, id, name, family):
        """
        Initialize a Student object.

        Args:
            id (int): The unique ID of the student.
            name (str): The first name of the student.
            family (str): The family name of the student.
        """
        self.id = id
        self.name = name
        self.family = family
        self.courses = []
    def __eq__(self, other):
        """
        Compare the student with another Student object or an integer ID.

        Args:
            other (Student or int): The object or student ID to compare with.

        Returns:
            bool: True if the student IDs are equal, otherwise False.
        """
        if isinstance(other, Student):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
    def __str__(self):
        """
        Return a formatted string containing the student's information.

        Returns:
            str: The student's ID, name, and family name.
        """
        return f"{self.id}\t{self.name}\t{self.family}"
    def print_info(self):
        """
        Print the student's information and enrolled courses.
        """
        print("Id:", self.id)
        print("Name:", self.name)
        print("Family:", self.family)
        print("Courses:")
        print("Id\tName\tUnit\tScore")
        for s in self.courses:
            print(s)
class Teacher:
    """
    Represents a teacher with an ID, name, family name, and courses.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course] = []
    def __init__(self, id, name, family):
        """
        Initialize a Teacher object.

        Args:
            id (int): The unique ID of the teacher.
            name (str): The first name of the teacher.
            family (str): The family name of the teacher.
        """
        self.id = id
        self.name = name
        self.family = family
        self.courses = []
    def __eq__(self, other):
        """
        Compare the teacher with another Teacher object or an integer ID.

        Args:
            other (Teacher or int): The object or teacher ID to compare with.

        Returns:
            bool: True if the teacher IDs are equal, otherwise False.
        """
        if isinstance(other, Teacher):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
    def __str__(self):
        """
        Return a formatted string containing the teacher's information.

        Returns:
            str: The teacher's ID, name, and family name.
        """
        return f"{self.id}\t{self.name}\t{self.family}"
    def print_info(self):
        """
        Print the teacher's information and assigned courses.
        """
        print("Id:", self.id)
        print("Name:", self.name)
        print("Family:", self.family)
        print("Courses:")
        print("Id\tName\tUnit\tScore") 
        for s in self.courses:
            print(s)
class Classroom:
    """
    Represents a classroom with a course, teacher, and list of students.
    """
    id: int = 0
    name: str = ""
    course: Course = None
    teacher: Teacher = None
    students: list[Student] = []
    def __init__(self, id, name):
        """
        Initialize a Classroom object.

        Args:
            id (int): The unique ID of the classroom.
            name (str): The name of the classroom.
        """
        self.id = id
        self.name = name
        self.students = []
    def __eq__(self, other):
        """
        Compare the classroom with another Classroom object or an integer ID.

        Args:
            other (Classroom or int): The object or classroom ID to compare with.

        Returns:
            bool: True if the classroom IDs are equal, otherwise False.
        """
        if isinstance(other, Classroom):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
    def __str__(self):
        """
        Return a formatted string containing the classroom information.

        Returns:
            str: The classroom ID and name.
        """
        return f"{self.id}\t{self.name}"
    def print_info(self):
        """
        Print the classroom's information, course, teacher, and students.
        """
        print("Id:", self.id)
        print("Name:", self.name)
        print("Courses:", self.course.id)
        print("Teachers:", self.teacher)
        print("Students:")
        print("Id\tName\tFamily")
        for s in self.students:
            print(s)
class School:
    """
    Represents a school with students, teachers, courses, and classrooms.
    """
    id: int = 0
    name: str = ""
    selected_classroom: Classroom = None
    selected_student: Student = None
    courses: list[Course] = []
    students: list[Student] = []
    teachers: list[Teacher] = []
    classrooms: list[Classroom] = []
    def __init__(self, id, name):
        """
        Initialize a School object.

        Args:
            id (int): The unique ID of the school.
            name (str): The name of the school.
        """
        self.id = id
        self.name = name
        self.courses = []
        self.students = []
        self.teachers = []
        self.classrooms = []
    def add_classroom(self, id, name, course_id, teacher_id, student_id):
        """
        Add a new classroom to the school.

        Args:
            id (int): The unique ID of the classroom.
            name (str): The name of the classroom.
            course_id (int): The ID of the course assigned to the classroom.
            teacher_id (int): The ID of the teacher assigned to the classroom.
            student_id (int): The ID of the student assigned to the classroom.
        """
        if id in self.classrooms:
            print(Fore.RED + "This Id Alredy Exsits" + Style.RESET_ALL)
            return
        if course_id not in self.courses:
            print(Fore.RED + "This Course Not Found" + Style.RESET_ALL)
            return
        if teacher_id not in self.teachers:
            print(Fore.RED + "This Teacher Not Found" + Style.RESET_ALL)
            return
        if student_id not in self.students:
            print(Fore.RED + "This Student Not Found" + Style.RESET_ALL)
            return
        course = self.courses[self.courses.index(course_id)]
        teacher = self.teachers[self.teachers.index(teacher_id)]
        student = self.students[self.students.index(student_id)]
        new_class = Classroom(id, name)
        new_class.course = course
        new_class.teacher = teacher
        new_class.students.append(student)
        self.classrooms.append(new_class)
        print(Fore.GREEN + "Classroom Added Successfully" + Style.RESET_ALL)
    def add_student(self, id, name, family):
        """
        Add a new student to the school.

        Args:
            id (int): The unique ID of the student.
            name (str): The first name of the student.
            family (str): The family name of the student.
        """
        if id in scl.students:
            print(Fore.RED + "This Id Alredy Exsits" + Style.RESET_ALL)
        else:
            self.students.append(Student(id, name, family))
            print(Fore.GREEN + "Student Added Successfully" + Style.RESET_ALL)
    def add_teacher(self, id, name, family):
        """
        Add a new teacher to the school.

        Args:
            id (int): The unique ID of the teacher.
            name (str): The first name of the teacher.
            family (str): The family name of the teacher.
        """
        if id in scl.teachers:
            print(Fore.RED + "This Id Alredy Exsits" + Style.RESET_ALL)
        else:
            self.teachers.append(Teacher(id, name, family))
            print(Fore.GREEN + "Teacher Added Successfully" + Style.RESET_ALL)
    def add_course(self, id, name, units, score):
        """
        Add a new course to the school.

        Args:
            id (int): The unique ID of the course.
            name (str): The name of the course.
            units (int): The number of course units.
            score (int): The score associated with the course.
        """
        if id in scl.courses:
            print(Fore.RED + "This Id Alredy Exsits" + Style.RESET_ALL)
        else:
            self.courses.append(Course(id, name, units, score))
            print(Fore.GREEN + "Course Added Successfully" + Style.RESET_ALL)
    def add_course_to_selected_student(self, id):
        """
        Add a course to the selected student's course list.

        Args:
            id (int): The ID of the course to add.
        """
        if id not in self.courses:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            if id in self.selected_student.courses:
                print(Fore.RED + "This Id Alredy Exsits" + Style.RESET_ALL)
            else:
                scl.selected_student.courses.append(
                    self.courses[self.courses.index(id)]
                )
                print(Fore.GREEN + "Course Added Successfully" + Style.RESET_ALL)
    def add_course_to_selected_teacher(self, id):
        """
        Add a course to the selected teacher's course list.

        Args:
            id (int): The ID of the course to add.
        """
        if id not in self.courses:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            if id in self.selected_teachers.courses:
                print(Fore.RED + "This Id Alredy Exsits" + Style.RESET_ALL)
            else:
                self.selected_teachers.courses.append(
                    self.courses[self.courses.index(id)]
                )
                print(Fore.GREEN + "Course Added Successfully" + Style.RESET_ALL)
    def remove_student(self, id):
        """
        Remove a student from the school.

        Args:
            id (int): The ID of the student to remove.
        """
        if id not in scl.students:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.students.remove(Student(id, "", ""))
            print(Fore.GREEN + "Student Deleted Successfully" + Style.RESET_ALL)
    def remove_teacher(self, id):
        """
        Remove a teacher from the school.

        Args:
            id (int): The ID of the teacher to remove.
        """
        if id not in scl.teachers:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.teachers.remove(Teacher(id, "", ""))
            print(Fore.GREEN + "Teacher Deleted Successfully" + Style.RESET_ALL)
    def remove_course(self, id):
        """
        Remove a course from the school.

        Args:
            id (int): The ID of the course to remove.
        """
        if id not in scl.courses:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.courses.remove(Course(id, "", 0, 0))
            print(Fore.GREEN + "Course Deleted Successfully" + Style.RESET_ALL)
    def remove_classroom(self, id):
        """
        Remove a classroom from the school.
        Args:
        id (int): The ID of the classroom to remove.
        """
        if id not in self.classrooms:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.classrooms.remove(Classroom(id, ""))
            print(Fore.GREEN + "Classroom Deleted Successfully" + Style.RESET_ALL)
    def remove_course_to_selected_student(self, id):
        """
        Remove a course from the selected student's course list.

        Args:
            id (int): The ID of the course to remove.
        """
        if id not in  self.selected_student.courses:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.selected_student.courses.remove(
                self.courses[self.courses.index(id)]
            )
            print(Fore.GREEN + "Course Deleted Successfully" + Style.RESET_ALL)
    def remove_course_to_selected_teacher(self, id):
        """
        Remove a course from the selected teacher's course list.

        Args:
            id (int): The ID of the course to remove.
        """
        if id not in self.selected_teachers.courses:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.selected_teachers.courses.remove(
                self.courses[self.courses.index(id)]
            )
            print(Fore.GREEN + "Course Deleted Successfully" + Style.RESET_ALL)
    def remove_student_from_classroom(self , id):
        if student_id not in scl.selected_classroom.students:
            print(Fore.RED + "This Student's Doesn't Exsits In This Classroom" + Style.RESET_ALL)
        else:
            scl.selected_classroom.students.remove(Student(student_id,"",""))
            print(Fore.GREEN + "Student Deleted Successfully" + Style.RESET_ALL)
    def edit_student(self, id, name, family):
        """
        Edit an existing student's information.

        Args:
            id (int): The ID of the student to edit.
            name (str): The new first name of the student.
            family (str): The new family name of the student.
        """
        if id not in scl.students:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.students[self.students.index(Student(id, "", ""))] = Student(
                id, name, family
            )
            print(Fore.GREEN + "Student Updated Successfully" + Style.RESET_ALL)
    def edit_teacher(self, id, name, family):
        """
        Edit an existing teacher's information.

        Args:
            id (int): The ID of the teacher to edit.
            name (str): The new first name of the teacher.
            family (str): The new family name of the teacher.
        """
        if id not in scl.teachers:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.teachers[self.teachers.index(Teacher(id, "", ""))] = Teacher(
                id, name, family
            )
            print(Fore.GREEN + "Teacher Updated Successfully" + Style.RESET_ALL)
    def edit_course(self, id, name, units, score):
        """
        Edit an existing course's information.

        Args:
            id (int): The ID of the course to edit.
            name (str): The new name of the course.
            units (int): The new number of course units.
            score (int): The new score of the course.
        """
        if id not in scl.courses:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.courses[self.courses.index(Course(id, "", 0, 0))] = Course(
                id, name, units, score
            )
            print(Fore.GREEN + "Course Updated Successfully" + Style.RESET_ALL)
    def edit_classrooms(self , id):
        if id  not in self.classrooms:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            name=input("name:")
            self.classrooms[self.classrooms.index(Classroom(id,""))]=Classroom(id,name)
            print(Fore.GREEN + "Classroom Updated Successfully" + Style.RESET_ALL)
    def print_student(self):
        """
        Print a list of all students in the school.
        """
        if len(self.students) == 0:
            print(Fore.RED + "No Student Added" + Style.RESET_ALL)
        else:
            print("Id\tName\tFamily")
            for t in scl.students:
                print(t)
    def print_teacher(self):
        """
        Print a list of all teachers in the school.
        """
        if len(self.teachers) == 0:
            print(Fore.RED + "No Teacher Added" + Style.RESET_ALL)
        else:
            print("Id\tName\tFamily")
            for s in scl.teachers:
                print(s)
    def print_course(self):
        """
        Print a list of all courses in the school.
        """
        if len(self.courses) == 0:
            print(Fore.RED + "No Course Added" + Style.RESET_ALL)
        else:
            print("Id\tName\tUnits\tScore")
            for c in scl.courses:
                print(c)
    def print_classrooms(self):
        """
        Print a list of all classrooms in the school.
        """
        if len(self.classrooms) == 0:
            print(Fore.RED + "No Classrooms Added" + Style.RESET_ALL)
        else:
            print("Id\tname")
            for c in scl.classrooms:
                print(c)
    def select_student(self, id):
        """
        Select a student by their ID.

        Args:
            id (int): The ID of the student to select.
        """
        if id not in self.students:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.selected_student = self.students[
                self.students.index(Student(id, "", ""))
            ]
            print(Fore.GREEN + "Student Selected Successfully" + Style.RESET_ALL)
    def select_teacher(self, id):
        """
        Select a teacher by their ID.

        Args:
            id (int): The ID of the teacher to select.
        """
        if id not in self.teachers:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            self.selected_teachers = self.teachers[
                self.teachers.index(Teacher(id, "", ""))
            ]
            print(Fore.GREEN + "Teacher Selected Successfully" + Style.RESET_ALL)
    def select_classroom(self, id):
        """
        Select a classroom by its ID.

        Args:
            id (int): The ID of the classroom to select.
        """
        if id not in scl.classrooms:
            print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
        else:
            scl.selected_classroom = scl.classrooms[
                scl.classrooms.index(Classroom(id, ""))
            ]
            print(Fore.GREEN + "Classroom Selected Successfully" + Style.RESET_ALL)
    def load_data(self):
        """
        Load school data from the data.json file.

        Reads courses, students, teachers, and classrooms from
        the JSON file and adds them to the school's data.
        """
        f1 = open("data.json", "rt")
        s = f1.read()
        f1.close()
        reads = json.loads(s)
        for item in reads["courses"]:
            self.courses.append(
                Course(item["id"], item["name"], item["units"], "")
            )
        for item in reads["students"]:
            t = Student(item["id"], item["name"], item["family"])
            for course_id in item["courses"]:
                if course_id[0] in self.courses:
                    y = self.courses[self.courses.index(course_id[0])]
                    y.score = course_id[1]
                    k = copy.deepcopy(y)
                    t.courses.append(k)
            self.students.append(t)
        for item in reads["teachers"]:
            t = Teacher(item["id"], item["name"], item["family"])
            for course_id in item["courses"]:
                if course_id in self.courses:
                    y = self.courses[self.courses.index(course_id)]
                    t.courses.append(y)
            self.teachers.append(t)
        for item in reads["classrooms"]:
            t = Classroom(item["id"], item["name"])
            if item["course"] in self.courses:
                t.course = self.courses[
                    self.courses.index(item["course"])
                ]
            if item["teacher"] is None:
                t.teacher = None
            elif item["teacher"] in self.teachers:
                t.teacher = self.teachers[
                    self.teachers.index(item["teacher"])
                ]
            for student in item["students"]:
                t.students.append(
                    self.students[self.students.index(student)]
                )
            self.classrooms.append(t)
    def save_data(self):
        """
        Save the school's data to the data.json file.

        Collects information about students, teachers, courses,
        and classrooms and stores it in JSON format.
        """
        result = {}
        result["students"] = []
        for student in self.students:
            result["students"].append({
                "id": student.id,
                "name": student.name,
                "family": student.family,
                "courses": [[c.id, c.score] for c in student.courses]
            })
        result["teachers"] = []
        for teacher in self.teachers:
            result["teachers"].append({
                "id": teacher.id,
                "name": teacher.name,
                "family": teacher.family,
                "courses": [c.id for c in teacher.courses]
            })
        result["courses"] = []
        for course in self.courses:
            result["courses"].append({
                "id": course.id,
                "name": course.name,
                "units": course.units
            })
        result["classrooms"] = []
        for c in self.classrooms:
            result["classrooms"].append({
                "id": c.id,
                "name": c.name,
                "course": c.course.id,
                "teacher": None if c.teacher is None else c.teacher.id,
                "students": [s.id for s in c.students]
            })
        with open("data.json", "w") as f:
            json.dump(result, f)
        print(Fore.GREEN + "Data Saved Successfully" + Style.RESET_ALL)
level="root"
scl=School(10,"sama")
scl.load_data( )
while True:
    if level=="root":
        print("1.students")
        print("2.teachers")
        print("3.courses")
        print("4.classrooms")
        print("5.save")
        print(Fore.RED + "1.exit" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"
        elif cmd==4:
            level="classrooms"
        elif cmd==5: 
            scl.save_data()
        elif cmd==0:
            break
    elif level=="students":
        print(Fore.YELLOW + "1. Show Students" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Students" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Edit Students" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Delete Students" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Select Students" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_student( )
        elif cmd==2:
            scl.print_student( )
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.add_student(i,n,f)
        elif cmd==3:
            scl.print_student( )
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.edit_student(i,n,f)
        elif cmd==4:
            scl.print_student( )
            id=int(input("id:"))
            scl.remove_student(id)
        elif cmd==5:
            scl.print_student( )
            id=int(input("id:"))
            scl.select_student(id)
            level="select students"
        elif cmd==0:
            level="root"
    elif level=="select students":
        print(Fore.YELLOW + "1. Show Info" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Courses" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Delete Courses" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Set Scores" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.selected_student.print_info()
        elif cmd==2:
            for c in scl.courses:
                print(c)
            id=int(input("id:"))
            scl.add_course_to_selected_student(id)
        elif cmd==3:
            for c in scl.selected_student.courses:
                print(c)
            id=int(input("id:"))
            scl.remove_course_to_selected_student(id)
        elif cmd==4:
            for course  in scl.selected_student.courses:
                score=int(input(f"{course.name}:"))
                course.score=score
        elif cmd==0:
            level="students"
    elif level=="teachers":
        print(Fore.YELLOW + "1. Show Teachers" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Teachers" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Edit Teachers" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Delete Teachers" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Select Teachers" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_teacher( )
        elif cmd==2:
            scl.print_teacher( )
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.add_teacher(i,n,f)
        elif cmd==3:
            scl.print_teacher( )
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.edit_teacher(i,n,f)
        elif cmd==4:
            scl.print_teacher( )
            id=int(input("Id:"))
            scl.remove_teacher(id)
        elif cmd==5:
            scl.print_teacher( )
            id=int(input("id:"))
            scl.select_teacher(id)
            level="select teachers"
        elif cmd==0:
            level="root"
    elif level=="select teachers":
        print(Fore.YELLOW + "1. Info" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Courses" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Delete Coursess" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.selected_teachers.print_info()
        elif cmd==2:
            for c in scl.courses:
                print(c)
            id=int(input("Id:"))
            scl.add_course_to_selected_teacher(id)
        elif cmd==3:
            for c in scl.selected_teachers.courses:
                print(c)
            id=int(input("Id:"))
            scl.remove_course_to_selected_teacher(id)
        elif cmd==0:
            level="teachers"
    elif level=="courses":
        print(Fore.YELLOW + "1. Show Courses" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Courses" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Edit Scores" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Delete Courses" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_course( )
        elif cmd==2:
            scl.print_course( )
            i=int(input("Id:"))
            n=input("Name:")
            u=input("Units:")
            s=input("Score:")
            scl.add_course(i,n,u,s)
        elif cmd==3:
            scl.print_course( )
            i=int(input("Id:"))
            n=input("Name:")
            u=input("Units:")
            s=input("Score:")
            scl.edit_course(i,n,u,s)
        elif cmd==4:
            scl.print_course( )
            id=int(input("Id:"))
            scl.remove_course(id)
        elif cmd==0:
            level="root"
    elif level=="classrooms":
        print(Fore.YELLOW + "1. Show Classrooms" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Classrooms" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Edit Classrooms" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Delete Classrooms" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Select Classrooms" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_classrooms()
        elif cmd==2:
            id=int(input("Id:"))
            name=input("Name:")
            for c in scl.courses:
                print(c.id,c.name)
            course_id=int(input("course_id:"))
            for t in scl.teachers:
                if course_id in t.courses:
                    print(t)
            teacher_id=int(input("id:"))
            for s in scl.students:
                if course_id in s.courses:
                    f=s.courses.index(course_id)
                    if s.courses[f].score<10:
                        print(s)
            student_id=int(input("id:"))
            scl.add_classroom(id,name,course_id,teacher_id,student_id)
        elif cmd==3:
            scl.print_classrooms( )
            id=int(input("Id:"))
            scl.edit_classrooms(id)
        elif cmd==4:
            scl.print_classrooms( )
            id=int(input("Id:"))
            scl.remove_classroom(id)
        elif cmd==5:
            scl.print_classrooms( )
            id=int(input("id:"))
            scl.select_classroom(id)
            level="select classrooms"
        elif cmd==0:
            level="root"
    elif level=="select classrooms":
        print(Fore.YELLOW + "1. Info" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Add Student" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Delete Student" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Change Courses" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Change Teacher" + Style.RESET_ALL)
        print(Fore.YELLOW + "6. Close Classroom" + Style.RESET_ALL)
        print(Fore.RED + "0. Back" + Style.RESET_ALL)
        cmd=int(input(">>:"))
        if cmd==1:
            scl.selected_classroom.print_info()
        elif cmd==2:
            failed_students=[]
            for s in scl.students:
                for c in s.courses:
                    if s not in scl.selected_classroom.students:
                        if c.score < 10:
                            if s not in failed_students:
                                failed_students.append(s)
                                break
                if len(scl.selected_classroom.students)==3:
                    print(Fore.RED + "There Is No Student" + Style.RESET_ALL)
                    break
            for s in failed_students:
                print(s)
            student_id=int(input("id:"))
            if student_id not in scl.students:
                print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
            else:
                student=scl.students[scl.students.index(Student(student_id,"",""))]
                if student in scl.selected_classroom.students:
                    print(Fore.RED + "This Student  Exsits" + Style.RESET_ALL)
                else:
                    scl.selected_classroom.students.append(student)
                    print(Fore.GREEN + "Student Added Successfully" + Style.RESET_ALL)
        elif cmd==3:
            for s in scl.selected_classroom.students:
                print(s)
            student_id=int(input("id:"))
            scl.remove_student_from_classroom(id)
        elif cmd==4:
            for c in scl.courses:    
                print(c)
            course_id=int(input("course_id:"))
            if course_id not in scl.courses: 
                print(Fore.RED + "This Id Doesn't Exsits" + Style.RESET_ALL)
            else:
                scl.selected_classroom.course=scl.courses[scl.courses.index(course_id)]
                if scl.selected_classroom.teacher is not None:
                    if course_id not in scl.selected_classroom.teacher.courses:
                        scl.selected_classroom.teacher = None
        elif cmd==5:
            for t in scl.teachers:    
                if t.id!=scl.selected_classroom.teacher.id:
                    print(t) 
            teacher_id=int(input("id:"))
            scl.selected_classroom.teacher=scl.teachers[scl.teachers.index(Teacher(teacher_id,"",""))]
        elif cmd==6:
            pass
        elif cmd==0:
            level="classrooms"
            