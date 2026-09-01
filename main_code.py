import copy
import json
class Course:
    id:int=0
    name:str=""
    units:int=0
    score:int=0
    def __init__(self,id,name,units,score):
        self.id=id
        self.name=name
        self.units=units
        self.score=score
    def __eq__(self,other):
        if isinstance(other,Course):
            return self.id==other.id
        elif isinstance(other,int):
            return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.units}\t{self.score} " 
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Student):
            return self.id==other.id
        elif isinstance(other,int):
            return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"
    def print_info(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Family:",self.family)
        print("Courses:")
        print("Id\tName\tUnit\tScore") 
        for s in self.courses:
            print(s)
class Teacher:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Teacher):
            return self.id==other.id
        elif isinstance(other,int):
            return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"
    def print_info(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Family:",self.family)
        print("Courses:")
        print("Id\tName\tUnit\tScore") 
        for s in self.courses:
            print(s)
class Classroom:
    id:int=0
    name:str=""
    course:Course=None
    teacher:Teacher=None
    students:list[Student]=[]
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.students=[]
    def __eq__(self,other):
        if isinstance(other,Classroom):
            return self.id==other.id
        elif isinstance(other,int):
            return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}"
    def print_info(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Courses:",self.course.id)
        print("Teachers:",self.teacher)
        print("Students:")
        print("Id\tName\tFamily") 
        for s in self.students:
            print(s)
class School:
    id:int=0
    name:str=""
    selected_classroom:Classroom=None
    selected_student:Student=None
    courses:list[Course]=[]
    students:list[Student]=[]
    teachers:list[Teacher]=[]
    classrooms:list[Classroom]=[]
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.courses=[]
        self.students=[]
        self.teachers=[]
        self.classrooms=[]
    def add_classroom(self,id,name,course_id,teacher_id,student_id):
        if id in self.classrooms:
            print("This Id Exists")
            return
        if course_id not in self.courses:
            print("Course not found")
            return
        if teacher_id not in self.teachers:
            print("Teacher not found")
            return
        if student_id not in self.students:
            print("Student not found")
            return
        course=self.courses[self.courses.index(course_id)]
        teacher=self.teachers[self.teachers.index(teacher_id)]
        student=self.students[self.students.index(student_id)]
        new_class=Classroom(id,name)
        new_class.course=course
        new_class.teacher=teacher
        new_class.students.append(student)
        self.classrooms.append(new_class)
    def add_student(self,id,name,family):
        if id in scl.students:
            print("This id is exsits")
        else:
            self.students.append(Student(id,name,family))
    def add_teacher(self,id,name,family):
        if id in scl.teachers:
            print("This id is exsits")
        else:
            self.teachers.append(Teacher(id,name,family))
    def add_course(self,id,name,units,score):
        if id in scl.courses:
            print("This id is exsits")
        else:
            self.courses.append(Course(id,name,units,score))
    def remove_student(self,id):
        if id not in scl.students:
            print("This id doesn't exsits")
        else:
            self.students.remove(Student(id,"",""))
    def remove_teacher(self,id):
        if id not in scl.teachers:
            print("This id doesn't exsits")
        else:
            self.teachers.remove(Teacher(id,"",""))
    def remove_course(self,id):
        if id not in scl.courses:
            print("This id doesn't exsits")
        else:
            self.courses.remove(Course(id,"",0,0))
    def edit_student(self,id,name,family):
        if id  not in scl.students:
            print("This id doesn't exists")
        else:
            self.students[self.students.index(Student(id,"",""))]=Student(id,name,family)
    def edit_teacher(self,id,name,family):
        if id  not in scl.teachers:
            print("This id doesn't exists")
        else:
            self.teachers[self.teachers.index(Teacher(id,"",""))]=Teacher(id,name,family)
    def edit_course(self,id,name,units,score):
        if id  not in scl.courses:
            print("This id doesn't exists")
        else:
            self.courses[self.courses.index(Course(id,"",0,0))]=Course(id,name,units,score)
    def print_student(self):
        if len(self.students)==0:
            print("No Student Added")
        else:
            print("Id\tName\tFamily") 
            for t in scl.students:
                print(t)
    def print_teacher(self):
        if len(self.teachers)==0:
            print("No Teacher Added")
        else:
            print("Id\tName\tFamily") 
            for s in scl.teachers:
                print(s)
    def print_course(self):
        if len(self.courses)==0:
            print("No Courses Added")
        else:
            print("Id\tName\tUnits\tScore") 
            for c in scl.courses:
                print(c)
    def print_classrooms(self):
        if len(self.classrooms)==0:
            print("No Classroom Added")
        else:
            print("Id\tname")
            for c in scl.classrooms:
                print(c)
    def load_data(self):
        f1=open("data.json","rt")
        s=f1.read( )
        f1.close( )
        reads=json.loads(s)
        for item in reads["courses"]:
            self.courses.append(Course(item["id"],item["name"],item["units"],""))     
        for item in reads["students"]:
            t = Student(item["id"],item["name"],item["family"])
            for course_id in item["courses"]:
                if course_id[0] in self.courses:
                    y=self.courses[self.courses.index(course_id[0])]
                    y.score=course_id[1]
                    k=copy.deepcopy(y)
                    t.courses.append(k)
            self.students.append(t)
        for item in reads["teachers"]:
            t = Teacher(item["id"],item["name"],item["family"])
            for course_id in item["courses"]:
                if course_id in self.courses:
                    y=self.courses[self.courses.index(course_id)]
                    t.courses.append(y)
            self.teachers.append(t)
        for item in reads["students"]:
            t = Student(item["id"],item["name"],item["family"])
            for course_id in item["courses"]:
                if course_id[0] in self.courses:
                    y=self.courses[self.courses.index(course_id[0])]
                    y.score=course_id[1]
                    k=copy.deepcopy(y)
                    t.courses.append(k)
            self.students.append(t)
        for item in reads["classrooms"]:
            t = Classroom(item["id"],item["name"])
            if item["course"] in self.courses:
                t.course=self.courses[self.courses.index(item["course"])]
            if item["teacher"] in self.teachers:
                t.teacher=self.teachers[self.teachers.index(item["teacher"])]
            for student in item["students"]:
                t.students.append(self.students[self.students.index(student)])
            self.classrooms.append(t)                              
    def save_data(self):
        result = {}
        result["students"] = []
        for student in self.students:
            result["students"].append({
                "id" : student.id,
                "name" : student.name,
                "family" : student.family,
                "courses" : [[c.id,c.score] for c in student.courses]
            })
        result["teachers"] = []
        for teacher in self.teachers:
            result["teachers"].append({
                "id": teacher.id,
                "name": teacher.name,
                "family": teacher.family,
                "courses" : [c.id for c in teacher.courses]
            })
        result["courses"] = []
        for course in self.courses:
            result["courses"].append({
                "id": course.id,
                "name": course.name,
                "units": course.units
            })
        result["classrooms"] =[]
        for c in self.classrooms:
            result["classrooms"].append({
                "id" :c.id,
                "name" : c.name,
                "course" : c.course.id,
                "teacher" : c.teacher.id,
                "students" : [s.id for s in c.students]
            })
        with open("data.json", "w") as f:
            json.dump(result, f)
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
        print("0.exit")
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
        print("1.show students")
        print("2.add students")
        print("3.edit students")
        print("4.delete students")
        print("5.select students")
        print("0.back")
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_student( )
        elif cmd==2:
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.add_student(i,n,f)
        elif cmd==3:
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.edit_student(i,n,f)
        elif cmd==4:
            id=int(input("id:"))
            scl.remove_student(id)
        elif cmd==5:
            scl.print_student( )
            id=int(input("id:"))
            if id not in scl.students:
                print("Error")
            else:
                scl.selected_student=scl.students[scl.students.index(Student(id,"",""))]
                level="select students"
        elif cmd==0:
            level="root"
    elif level=="select students":
        print("1.info")
        print("2.add courses")
        print("3.delete courses")
        print("4.set scorses")
        print("0.back")
        cmd=int(input(">>:"))
        if cmd==1:
            scl.selected_student.print_info()
        elif cmd==2:
            for c in scl.courses:
                print(c)
            t=int(input("id:"))
            if t  not in scl.courses:
                print("This id doesn't exist")
            else:
                if t in scl.selected_student.courses:
                    print("This id already exist")
                else:
                    scl.selected_student.courses.append(scl.courses[scl.courses.index(t)])
        elif cmd==3:
            for c in scl.selected_student.courses:
                print(c)
            t=int(input("id:"))
            if t not in scl.courses:
                print("This id doesn't exists")
            else:
                scl.selected_student.courses.remove(scl.courses[scl.courses.index(t)])
        elif cmd==4:
            for course  in scl.selected_student.courses:
                score=int(input(f"{course.name}:"))
                course.score=score
        elif cmd==0:
            level="students"
    elif level=="teachers":
        print("1.show teachers")
        print("2.add teachers")
        print("3.edit teachers")
        print("4.delete teachers")
        print("5.select teachers")
        print("0.back")
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_teacher( )
        elif cmd==2:
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.add_teacher(i,n,f)
        elif cmd==3:
            i=int(input("Id:"))
            n=input("Name:")
            f=input("Family:")
            scl.edit_teacher(i,n,f)
        elif cmd==4:
            id=int(input("Id:"))
            scl.remove_teacher(id)
        elif cmd==5:
            scl.print_teacher( )
            id=int(input("id:"))
            if id not in scl.teachers:
                print("This id doesn't exists")
            else:
                scl.selected_teachers=scl.teachers[scl.teachers.index(Teacher(id,"",""))]
                level="select teachers"
        elif cmd==0:
            level="root"
    elif level=="select teachers":
        print("1.info")
        print("2.add courses")
        print("3.delete courses")
        print("0.back")
        cmd=int(input(">>:"))
        if cmd==1:
            scl.selected_teachers.print_info()
        elif cmd==2:
            for c in scl.courses:
                print(c)
            t=int(input("Id:"))
            if t  not in scl.courses:
                print("This id doesn't exist")
            else:
                if t in scl.selected_teachers.courses:
                    print("This id already exist")
                else:
                    scl.selected_teachers.courses.append(scl.courses[scl.courses.index(t)])
        elif cmd==3:
            for c in scl.selected_teachers.courses:
                print(c)
            t=int(input("Id:"))
            if t not in scl.courses:
                print("This id doesn't exists")
            else:
                scl.selected_teachers.courses.remove(scl.courses[scl.courses.index(t)])
        elif cmd==0:
            level="teachers"
    elif level=="courses":
        print("1.show courses")
        print("2.add courses")
        print("3.edit courses")
        print("4.delete courses")
        print("0.back")
        cmd=int(input(">>:"))
        if cmd==1:
            scl.print_course( )
        elif cmd==2:
            i=int(input("Id:"))
            n=input("Name:")
            u=input("Units:")
            s=input("Score:")
            scl.add_course(i,n,u,s)
        elif cmd==3:
            i=int(input("Id:"))
            n=input("Name:")
            u=input("Units:")
            s=input("Score:")
            scl.edit_course(i,n,u,s)
        elif cmd==4:
            id=int(input("Id:"))
            scl.remove_course(id)
        elif cmd==0:
            level="root"
    elif level=="classrooms":
        print("1.show classrooms")
        print("2.add classrooms")
        print("3.edit classrooms")
        print("4.delete classrooms")
        print("5.select classrooms")
        print("0.back")
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
            if id  not in scl.classrooms:
                print("This id doesn't exists")
            else:
                name=input("name:")
                scl.classrooms[scl.classrooms.index(Classroom(id,""))]=Classroom(id,name)
        elif cmd==4:
            scl.print_classrooms( )
            id=int(input("Id:"))
            if id not in scl.classrooms:
                print("This id doesn't exsits")
            else:
                scl.classrooms.remove(Classroom(id,""))
        elif cmd==5:
            scl.print_classrooms( )
            id=int(input("id:"))
            if id  not in scl.classrooms:
                print("This id doesn't exists") 
            scl.selected_classroom=scl.classrooms[scl.classrooms.index(Classroom(id,""))]
            level="select classrooms"
        elif cmd==0:
            level="root"
    elif level=="select classrooms":
        print("1.info")
        print("2.add student")
        print("3.delete student")
        print("4.change course")
        print("5.change teacher")
        print("6.close classroom")
        print("0.back")
        cmd=int(input(">>:"))
        if cmd==1:
            scl.selected_classroom.print_info()
        elif cmd==2:
            for s in scl.students:
                for c in s.courses:
                    if c.score< 10:
                        print(s.id,s.name)
            student_id=int(input("id:"))
            scl.add_classroom(id,"-","-","-",student_id)
        elif cmd==3:
            pass
        elif cmd==4:
            for c in scl.courses:    
                print(c)
            course_id=int(input("course_id:"))
            if course_id not in scl.courses: 
                print("This id doesn't exists")
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