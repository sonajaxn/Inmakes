class student:
    def __init__(self,name,mark,subject,gender):
        self.name=name
        self.mark=mark
        self.subject=subject
        self.gender=gender
    def getDetails(self):
        print(self.name,self.mark)
    def studentMotto(self):
        print ("i love my parents")

class parents(student):
    def __init__(self,name,stdname,gender):
        self.name=name
        self.stdname=stdname
        self.gender=gender
    def getDetails(self):
        print(self.name,self.stdname)
    def parentMotto(self):
        print ("i love my kid")


pr1=parents('james','jack','m')
pr1.studentMotto()




# st1=student('jacky',100,'maths','m')
# st1.getDetails()
# pr1=parents('james',st1.name,'m')
# pr1.getDetails()
# st2=student('sona',10,'maths','bi')
# total=st1.mark+st2.mark
# print ("total = "+str(total)
#        )

# print (dir(st1))
# print (st1.name)
# print (st1.mark)
# print (getattr(st1,"gender"))
