class employee1:
    org_name = "DAC"
								
		def __init__(self,emp_name,emp_id,emp_salary):
			self.emp_name = emp_name
			self.emp_id = emp_id
			self.salary = emp_salary
										
		def get_emp_details(self):
			print("Emp-name is:- ",self.emp_name)
			print("Emp-id is -", self.emp_name)
			print("Emp-salary is",self.salary)

		@classmethod
		def set_org_name(cls):
			return employee1.org_name

class Manager(employee1):
	def __init__(self, emp_name, emp_id, emp_salary,designation,rcv_managed_employees):
		super().__init__(emp_name, emp_id, emp_salary)
		self.managed_employees = rcv_managed_employees
		self.designation = designation
        
	def get_manager_details(self):
		super().get_emp_details()
		print("all emp are: ", end= " ")
		for val in self.managed_employees:
			print(f"{val.name}",end=",")
e1=employee1("sandeep", 1, 10000 )
e2=employee1("komal",2, 20000)
e3=employee1("suraj",3, 3000)

m1= Manager ("jhon",20, 150000,"Manager",[e1,e2,e3])

m1.get_emp_details()
e1.get_emp_details()


