class hospital:
  def __init__(self):
    self.adminName=""
    self.docName=""
    self.sisterName=""
    self.dept=""
  def EnterHospDetails(self):
    print("\n")
    print("....Welcome to HospitalDetails Entry....")
    self.adminName=input("Enter admin name : ")
    self.docName=input("Enter doctor name : ")
    self.sisterName=input("Enter sister name : ")
    self.dept=input("Enter department name : ")
class department(hospital):  
  def PrintHospDetails(hospital):
    print("\n")
    print("....Welcome to HospitalDetails.....")
    print("Admin Name : "+hospital.adminName)
    print("Department Name : "+hospital.dept)
    print("Doctor Name : "+hospital.docName)
    print("Sister Name : "+hospital.sisterName)
class patientWard:
    def __init__(self):
        self.patientName=""
        self.patientAge=""
        self.patientNumber=""
        self.PatientDisease=""
    def EnterPatientDetails(self):
        print(".....Welcome to PatientWard Entry.....")
        self.patientName=input("Enter patientName : ")
        self.patientAge=input("Enter patientAge : ")
        self.patientNumber=input("Enter patientNumber : ")
        self.PatientDisease=input("Enter PatientDisease : ")        
    def PrintPatientDetails(self):
        print("Patient Name : "+self.patientName)
        print("Patient Number : "+self.patientNumber)
        print("Patient Age : "+self.patientAge)
        print("Patient Disease : "+self.PatientDisease)
obj=department()
obj.EnterHospDetails()
obj.PrintHospDetails()
obj2=patientWard()
obj2.EnterPatientDetails()
obj2.PrintPatientDetails()    
    
    


