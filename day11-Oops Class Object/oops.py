# # class Myclass:
# #     def myfunc(self):
# #         pass
# #     def mydisplay(self,name):
# #         print(name)
# #
# # mc1=Myclass()
# # mc1.myfunc()
# # mc1.mydisplay("hello")
# 
# 
# class Student:
# 
#     def details(self,name,rollno):
#         print("Student details:",name,rollno)
#     @staticmethod
#     def schoolname():
#         print("Geeta Vidyalayam")
# 
# stud1=Student()
# stud1.details("Karthik",20)
# stud1.schoolname()
# 
# stud2=Student()
# stud2.details("Akhil",21)
# # stud2.schoolname()  

class Myclass:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print(self.name,self.rollno)
        
stu1=Myclass('karthik',20)
stu2=Myclass('Akhil',50)

stu1.display()
stu2.display()