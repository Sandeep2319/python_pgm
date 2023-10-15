
class Employee:
    org_name="CDAC"
    @classmethod
    def get_org_name(cls):
        return Employee.org_name
    @classmethod
    def set_org_name(cls):
        i=input("Enter Organization Name :")
        Employee.org_name=i
    #intialize the value
    
    def __init__(self,emp_id,name,base_location,deployed_location,designation,salary):
        self.emp_id=emp_id
        self.name=name
        self.base_location=base_location
        self.deployed_location=deployed_location
        self.designation=designation
        self.salary =salary
    def get_employee_details(self):
        print("Employee ID :",self.emp_id)
        print("Employee Name :",self.name)
        print("Employee Base Location :",self.base_location)
        print("Employee Deployed Location :",self.deployed_location)
        print("Employee Designation :",self.designation)
    
   
class Manager(Employee):
	
	# -- instance variables and methods()
    def __init__(self,rcv_emp_id,rcv_name,rcv_base_location,rcv_deployed_location,rcv_designation,rcv_salary,rcv_managed_employees):
        super().__init__(rcv_emp_id,rcv_name,rcv_base_location,rcv_deployed_location,rcv_designation,rcv_salary)
        self.managed_employees= rcv_managed_employees
        
    def perform_appraisal_for_an_employee(self,emp_obj,percent_raise):
        current_salary= emp_obj.salary
        increment = current_salary * percent_raise / 100
        emp_obj.salary = current_salary+ int(increment)
    
    def get_manager_details(self):
        #self.get_employee_details() # because I overrided in Manager I had comment this 
        super().get_employee_details()
        print("Managed employees:  ",end = " ")
        for val in self.managed_employees:
            print(f"{val.name}",end =",")
        
# main method
#create 3 objects of Employee 
e1 = Employee(100,"Gaurav","Pune","Bangalore","Developer",100)
e2 = Employee(200,"Pratik","Chennai","Bangalore","Senior Developer",200)
e3 = Employee(300,"Hemant","Delhi","Bangalore","Architect",300)

#create an object of Manager_class and add the above 3 employee objects created as managed employees 
m1= Manager(400,"Elon Musk","California","Pune","Manager",1000,[e1,e2,e3])

# display get_manager_details()
m1.get_manager_details()

#for an employee do perform_appraisal_for_an_employee()
print( "\n-----------------------------------\nBefore Appraisal ")
e1.get_employee_details()
m1.perform_appraisal_for_an_employee(e1,100)
print( "-----------------------------------\nAfter Appraisal ")
e1.get_employee_details()

    
