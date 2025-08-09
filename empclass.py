class Employee:
    def __init__(self, name, age, designation, salary):
        self.name = name
        self.age = age
        self.designation = designation
        self._salary = salary  

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self._salary}")

   
    def get_salary(self):
        return self._salary

class SalaryCalculation(Employee):
    def increase_salary(self, amount):
        if amount > 0:
            self._salary += amount
            print(f"Salary increased by $={amount}")
        else:
            print("Increase amount must be positive.")

    def get_salary_info(self):
        print(f"Your current salary is: ${self._salary}")


emp = SalaryCalculation("Ajay", 20, "Programmer", 10000)
emp.get_info()
emp.get_salary_info()
emp.increase_salary(2000)
emp.get_salary_info()
