class hospital:
    def __init__(self,admin,doc,sister,dept):
        self.admin=admin
        self.doc=doc
        self.sister=sister
        self.dept=dept
    def getdetails(self):
        self.admin=input("enter admin name")
        self.doc=input("enter ur doc name")
        self.sister=input("enter ur nurse name")
        self.dept=input("what dept u are")
        print(self.admin,self.doc,self.sister,self.dept)

obj=hospital('','','','')
obj.getdetails()
