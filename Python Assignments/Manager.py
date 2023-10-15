class Manager:
        def __int__(self, emp_id, name, base_location, deployed_location, designation,  salary, get_employee_details):
        # instance variable
            self.rcv_emp_id = emp_id
            self.rcv_name = name
            self.rcv_base_location = base_location
            self.rcv_deployed_location = deployed_location
            self.rcv_designation = designation
            self.rcv_salary = salary
            
        print(f"{self}\n employee-id: - {emp_id}\n Name:- {name}\n Baese-Location :- {base_location}\n Deplyoed-Location : - {deployed_location}\n  Designation : - {designation}\n salary: - {salary}\n Emp_detail: -{get_employee_details}")
        
        
        
def main():
    print("I am in main funtion")
    
    Employee1 = company(1,"Sandeep","mumbai","Delhi","Manager",125000)
    Employee2 = company(2,"komal","mumbai","Delhi","Emp",125000)
    Employee2 = company(3,"Sandeep","mumbai","Delhi","Emp",125000)
    


class Manager(Employee):
        
        #initializer
        def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
            super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
            
if __name__ == "__main__":
    main()