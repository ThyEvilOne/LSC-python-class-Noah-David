my_list = []

def append_list():
    for i in range(6):
        my_list.append(input('Enter input:'))
    print(my_list)

    return my_list

def extend_list():
    print(my_list)
    for i in range(2):
        my_list.extend(input('Enter input to extend list:'))

    return my_list

def remove_item():
    print(my_list)
    my_list.remove(input('Enter item to remove:'))

    return my_list

def list_pop():
    my_list.pop()
    print(my_list)
    return my_list

def list_sort_reverse():
    my_list.sort
    print(my_list)

    my_list.reverse()
    print(my_list)

    return my_list

def list_index_count():
    print(my_list.index(input('Enter item to find place:')))

    print(my_list.count(input('Enter item to count times:')))

    return

append_list()
extend_list()
print(remove_item())
list_pop()
list_sort_reverse()
list_index_count()
