class college:
    collegename="LIET" #public variable
    address="alwar"
class faculty(college):
    __Salary="50k"   #private variable
    Branch="CS"
    
class student(faculty):
    name="sachin"    
    sem="4th"
    
    
    def disp(self):
        print(self.name)
        print(self.sem)
        print(self.Branch)
        print(self.collegename)
        print(self.address)

    def __int__(self):
        self.disp()

s=student()