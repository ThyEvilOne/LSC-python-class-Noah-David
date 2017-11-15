class Employee:
        def __init__(self, name, id_number, department, job_title):
                self.name = name
                self.id_number = id_number
                self.department = department
                self.job_title = job_title

        def __str__(self):
                return ('''
Name: %s
ID Number: %s
Department: %s
Job title: %s \n''' %(self.name, self.id_number, self.department, self.job_title))

employee_1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
employee_2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
employee_3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

print(employee_1, employee_2, employee_3)

