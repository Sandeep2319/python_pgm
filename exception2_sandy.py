class Employee2:
    org_name = "DAC"
    @classmethod
    def set_org_name(cls):
        i = input("Enter the organisation name:- ")
        return Employee2.i

    def __init__(self, emp_id, name ,base_location ,desired_location ,salary, designation):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.desired_location = desired_location
        self.salary = salary
        self.designation = designation
    def get_emp_details(self):
        print("Emp-Id is :" , self.emp_id)
        print("Emp-name is: ", self.name)
        print("Emp-base_location: -" , self.base_location)
        print("Emp-Salary is : " ,self.salary)
        print("Emp-designation :" ,self.designation)
        
class Manager(Employee2):
    e1 = 