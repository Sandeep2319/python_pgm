class emp:
    deptartment_name= "DHPCSA"
    
    #initializer 
    def __init__(self,emp_id,emp_salary,up_salary,mgr_id):
        #instance variable
        self.s_emp_id = emp_id
        self.s_emp_salary = emp_salary
        self.u_emp_salary = up_salary
        self.s_mgr_id = mgr_id
        
    
    #functions to call value
    def get_emp_id(self):
        return self.s_emp_id
    
    def get_emp_salary(self):
        return self.s_emp_salary

    def set_emp_salary(self):
        return self.u_emp_salary+10000
    
    def get_mgr_id(self):
        return self.s_mgr_id
        
    @staticmethod
    
    def field_expertise():
        print("Facilities are 1) python 2) c++\n")
    
    @classmethod
    
    def dept_name(cls, dept_name):
        cls.deptartment_name = dept_name
        

# Main body starts 
def  main():
    print("I am in main ")
    
    Employee1 = emp(1,10000,10000,23)
    Employee2 = emp(2,15000,10000,24)
    
    print("1st Employee info\n")
    print(Employee1.s_emp_id)
    
    print("Orignal the salary is :- ",Employee1.s_emp_salary)
    print("Updated the salary is :- ",Employee1.u_emp_salary+5000)
    print(Employee1.s_mgr_id)
    
    print("\n")
    
    print("2nd Employee info")
    print(Employee2.s_emp_id)
    print(Employee2.s_emp_salary)
    print(Employee2.u_emp_salary)
    print(Employee2.s_mgr_id)
    
    #To call class method 
    print("Department is: -" , emp.deptartment_name)
    
    # To called static methods 
    emp.field_expertise()
    
    
# invoke the main function 
if __name__ == "__main__":
    main()