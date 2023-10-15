class Employee1:
    org_name= "CDAC"
    @classmethod
    def set_org_name(cls):
        return Employee1.org_name
    @classmethod
    def set_org_name(cls):
        i = input("Enter the org name: ")
        return Employee1.i
    def __init__(self,emp_id,name,base_location,desired_location, salary,designation):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.desired_location = desired_location
        self.salary = salary
        self.designation =designation
        
    def get_emp_details(self):
        print("Emplyoee id is : -",self.emp_id)
        print("Employee Name is:-", self.name)
        print("Employe base_location is:- ", self.base_location)
        print("Employee desired location is:- ",self.desired_location)
        print("Employee salary is:- ",self.salary)
class Manager(Employee1):
    def __init__(self, emp_id, name, base_location, desired_location, salary,designation, rcv_managed_employees):
        super().__init__(emp_id, name, base_location, desired_location, salary,designation)
        self.managed_employees=rcv_managed_employees
        self.designation=designation
        
    def get_manager_details(self):
        super().get_emp_details()
        print("All employees are: ",end= " ")
        for val in self.managed_employees:
            print(f"{val.name}",end=",")

e1=Employee1(1,"sandeep","Mumbai","pune",10000,"manger")
e2=Employee1(1,"sandeep","Mumbai","pune",10000,"manger")
e3=Employee1(1,"sandeep","Mumbai","pune",10000,"manger")
    
m1 = Manager(400,"Chetan","California","pune",10000,"Manager",[e1,e2,e3])


m1.get_emp_details()
e1.get_emp_details()
            




        
        