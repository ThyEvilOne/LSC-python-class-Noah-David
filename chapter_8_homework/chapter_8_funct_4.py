my_dict = {'Hello': 1, 'World': 2}

def dict_clear():
    print(my_dict)
    my_dict.clear()
    print(my_dict)

def dict_get():
    print(my_dict.get(input('Enter key name:')))

def dict_update():
    my_dict.update({'!': 3})
    print(my_dict)

def dict_pop():
    my_dict.pop('!')
    print(my_dict)

dict_get()
dict_update()
dict_pop()
dict_clear()
