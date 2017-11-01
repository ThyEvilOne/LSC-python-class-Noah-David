phone_number = str(input('Enter phone number XXX-XXX-XXXX: '))

def translate():
    ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
    two = ['A', 'B', 'C']
    three = ['D', 'E', 'F']
    four = ['G', 'H', 'I']
    five = ['J', 'K', 'L']
    six = ['M', 'N', 'O']
    seven = ['P', 'Q', 'R', 'S']
    eight = ['T', 'U', 'V']
    nine = ['W', 'X', 'Y', 'Z']
    new_phone = phone_number[:]

    for i in new_phone:
        if i in ints:
            pass
        elif i == '-':
            pass
        elif i in two:
            new_phone = new_phone.replace(i, '2')
        elif i in three:
            new_phone = new_phone.replace(i, '3')
        elif i in four:
            new_phone = new_phone.replace(i, '4')
        elif i in five:
            new_phone = new_phone.replace(i, '5')
        elif i in six:
            new_phone = new_phone.replace(i, '6')
        elif i in seven:
            new_phone = new_phone.replace(i, '7')
        elif i in eight:
            new_phone = new_phone.replace(i, '8')
        elif i in nine:
            new_phone = new_phone.replace(i, '9')
        else:
            break

    print(new_phone)

translate()

    
    
