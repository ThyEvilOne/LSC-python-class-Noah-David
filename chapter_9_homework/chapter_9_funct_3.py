arg = ''
print('''
To look up employee enter: look up
To add new employee enter: add
To change employee enter: change
To delete employee enter: delete
Quit: q''')

class Employee:
        def __init__(self, name = '', ID = '', department = '',  job = ''):
                self.name = name
                self.ID = ID
                self.department = department
                self.job = job

                self.eployees = {}

        def add_eployee(self, name, ID, department, job):
                self.eployees[ID] = name, department, job

        def look_up(self, ID):
                return self.eployees.get(ID, 'RETRY LOOK UP')

        def change(self, ID):
                for i in self.eployees:
                        if ID == i:
                                print('ID found...')
                                self.eployees[ID] = input('Enter name: '), input('Enter department: '), input('Enter job: ')
                        else:
                                pass

        def delete(self, ID):
                del self.eployees[ID]
                print('Employee %s deleted...' %ID)
                        
def menu(arg):
        if arg == 'look up':
                print(employee.look_up(input('Enter employee ID: ')))
                
        elif arg == 'add':
                employee.add_eployee(input('Enter Name: '), input('Enter ID: '), input('Enter Department: '), input('Enter job: '))
                
        elif arg == 'change':
                employee.change(input('Enter id: '))
                
        elif arg == 'delete':
                employee.delete(input('Enter id(to delete): '))
        elif arg == 'q':
                return 'q'
        else:
                print('Unkown command...please retry command')

employee =Employee()

while(arg != 'q'):
        arg = menu(input('Please enter command: '))
        

