class Employee:
	organisation_name="CDAC"
 
	def get_organisation_name(self):
        print("hello")
    def set_organisation_name(org_name):
        i=input("Enter Organization Name :")
        Employee.org_name=i
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

# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	managed_employees[],
# 	perform_appraisal_for_an_employee(emp_id,percent_raise),
# 	get_manager_details(mgr_id)
# )

class Manager:
	
	# -- instance variables and methods()
 def __init__(self,managed_employees[]):
	self.managed_employees[]=managed_employees[]
	perform_appraisal_for_an_employee(emp_id,percent_raise),
	get_manager_details(mgr_id)
)
Write a main method that does the following:
create 3 objects of Employee 
create an object of Manager_class and add the above 3 employee objects created as managed employees 
display get_manager_details()
for an employee do perform_appraisal_for_an_employee()