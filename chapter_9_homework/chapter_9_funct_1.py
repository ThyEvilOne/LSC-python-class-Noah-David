class CellPhone:
        def __init__(self, manufact, model, retail_price):
                self.manufact = manufact
                self.model = model
                self.retail_price = retail_price

        def __str__(self):
                return('''Here is the data that you entered:
Manufacturer: %s
Model Number: %s
Retail Price: $%s''' %(self.manufact, self.model, self.retail_price))

        def set_manufact(self):
                self.manufact = input('Enter Manufacturer: ')

        def set_model(self):
                self.model = input('Enter Model number: ')

        def set_retail_price(self):
                self.retail_price = input('Enter Retail price: ')

        def get_manufact(self):
                return ('Manufacturer: %s') %self.manufact

        def get_model(self):
                return ('Model Number: %s') %self.model_number

        def get_retail_price(self):
                return ('Retail Price: %s') % self.retail_price

        

cellphone_info = CellPhone(input('Enter Manufacturer: '),  input('Enter the model number: '), input('Enter the retail price: '))

print(cellphone_info)

    
