class Employee:
    organisation_name = "ABC Company"  # class variable

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.salary = salary

    def get_organisation_name(self):
        return self.organisation_name

    def set_organisation_name(self, org_name):
        self.organisation_name = org_name

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}"


class Manager(Employee):
    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
        self.managed_employees = []

    def perform_appraisal_for_an_employee(self, emp_id, percent_raise):
        for employee in self.managed_employees:
            if employee.emp_id == emp_id:
                employee.salary *= (1 + percent_raise / 100)
                return f"Appraisal performed for Employee ID: {emp_id}. New salary: {employee.salary}"
        return "Employee not found."

    def get_manager_details(self, mgr_id):
        return f"Manager ID: {mgr_id}, Managed Employees: {[emp.emp_id for emp in self.managed_employees]}"


def main():
    emp1 = Employee(1, "John", "Office A", "Office B", "Software Engineer", 5000)
    emp2 = Employee(2, "Jane", "Office A", "Office C", "Product Manager", 7000)
    emp3 = Employee(3, "Mike", "Office B", "Office B", "Quality Assurance", 4500)

    manager = Manager(4, "Tom", "Office A", "Office A", "Engineering Manager", 10000)
    manager.managed_employees.extend([emp1, emp2, emp3])

    print(manager.get_manager_details(4))
    print(manager.perform_appraisal_for_an_employee(2, 10))
    print(emp2.get_employee_details())


if __name__ == "__main__":
    main()