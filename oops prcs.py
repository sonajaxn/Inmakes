class student:
    def __init__ (self):
        self.mark=0
        self.name=''
    def enterdetails(self):
        self.name = input("Enter your name: ")
        self.mark=int(input("enter ur mark"))
    def printdetail(self):
        print(self.mark,self.name)
obj=student()
obj.getdetails()
# obj.putdetails()

