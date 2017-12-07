#from moduleElement import *

class ModuleElement(object):

    def __init__(self,module):
        "constructor for class module element"

        # store module as instance variable
        self.module = module


    def add_important_date(self,kind,date):
        "add a date to the module's date dictionary"

        self.module.dates.append((kind,date))

################################################################################

class Lesson(ModuleElement):

    def __init__(self,module):
        "constructor for class lesson"

        # call super class constructor
        ModuleElement.__init__(self,module)


    def add_important_date(self,date):
        "add a lesson to the date dictionary"

        ModuleElement.add_important_date(self,"Lesson",date)

################################################################################

class Lab(ModuleElement):

    def __init__(self,module):
        "constructor for class lab"

        # call super class constructor
        ModuleElement.__init__(self,module)


    def add_important_date(self,date):
        "add a lab session to the date dictionary"

        ModuleElement.add_important_date(self,"Lab Session",date)

################################################################################

class Midterm(ModuleElement):

    def __init__(self,module):
        "constructor for class midterm"

        # call super class constructor
        ModuleElement.__init__(self,module)


    def add_important_date(self,date):
        "add a midterm to the date dictionary"

        ModuleElement.add_important_date(self,"Midterm",date)

################################################################################

class FinalExam(ModuleElement):

    def __init__(self,module):
        "constructor for class final exam"

        # call super class constructor
        ModuleElement.__init__(self,module)


    def add_important_date(self,date):
        "add a final exam to the date dictionary"

        ModuleElement.add_important_date(self,"Final Exam",date)

################################################################################

class Module(object):

    module_count = 0

    def __init__(self, ects, title, semester, grade=None):
        "constructor for class module"

        self.ects = ects
        self.grade = grade
        self.title = title
        self.semester = semester

        self.dates = []

        self.elements = []

        Module.module_count += 1

    def get_important_dates_overview(self):
        "prints all the important dates for a module"

        print("Important dates for {0:s}:".format(self.title))

        for kind, date in self.dates:
            print("\t{0:s} on {1:s}".format(kind, date))

    def set_grade(self, grade):
        "set the grade to a given value"

        self.grade = grade

    def add_module_element(self, other_class, date):
        "add a new module element to the elements list"

        obj = other_class(self)
        obj.add_important_date(date)
        self.elements.append(obj)

    def get_title(self):
        return self.title

    def get_grade(self):
        return self.grade


#########################################################################

class Course(Module):
    def __init__(self, ects, title, semester, grade=None):
        Module.__init__(self, ects, title, semester, grade)

    def __str__(self):
        return "Course: " + self.title

#########################################################################

class Seminar(Module):
    def __init__(self, ects, title, semester, topic, grade = None):
        Module.__init__(self, ects, title, semester, grade)
        self.topic = topic

    def __str__(self):
        return self.title + " under the topic: " + self.topic

    def get_topic(self):
        return self.topic

#########################################################################

class Thesis(Module):
    def __init__(self, ects, title, semester, topic, research_group, grade = None):
        Module.__init__(self, ects, title, semester, grade)
        self.research_group = research_group
        self.topic = topic

    def __str__(self):
        return "Bachelor Thesis on the topic: " + self.topic + " in the Research Group " + self.research_group

    def get_topic(self):
        return self.topic

    def get_research_group(self):
        return self.research_group

#########################################################################

#from module import *
#from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}


    def add_module(self,title):
        self.modules.append(title)
        self.grades[title] = Module.get_grade(title)

    def get_list_modules(self):
        print("Modules of Student " + str(self.name) + ":")
        for module in self.modules:
            print(module)

    def get_grades(self):
        print("Grades of Student " + str(self.name) + ":")
        for title in self.grades:
            print(str(title) + ": " + str(self.grades[title]))

#########################################################################

### test cases ###

info1 = Course(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
#info1.get_important_dates_overview()
# expected output:
# Important dates for Info 1:
#	Midterm on 31.10.2017
#	Final Exam on 20.12.2017
#print(info1)
# expected output:
# Course: Info 1

math1 = Course(6, "Mathematik I", 1)
math1.add_module_element(Midterm,"18.12.2017")
#math1.get_important_dates_overview()
# Important dates for Mathematik I:
#	Midterm on 18.12.2017


#print(Module.module_count)
# expected output: 2

thesis = Thesis(18,"Bachelor Thesis",6,"A promising research topic on Software Engineering","SEAL")
#print(thesis)
# expected output:
# Bachelor Thesison the topic: A promising research topic on Software Engineering in the Research Group SEAL


sem = Seminar(3,"Seminar in Software Engineering",4,"A Seminar topic")
#print(sem)
# print(thesis)
# expected output:
# Seminar in Software Engineering under the topic: A Seminar topic

info1.set_grade(6)

#########################################################################

### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
#me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

#me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
