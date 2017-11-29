# Type your code here
errorInt = 1
while errorInt == 1:
    user_service = str(input('Enter desired auto service:\n'))

    services = {'Oil change':35, 'Tire rotation':19, 'Car wash':7}
 
    if user_service == 'Oil change':
        output_serv = 'oil change'
    elif user_service == 'Tire rotation':
        output_serv = 'tire rotation'
    elif user_service == 'Car wash':
        output_serv = 'car wash'
    

    print('You entered:', user_service)

    #if user_service == 'Oil change' or user_service == 'Tire rotation' or user_service == 'Car wash':
    try:
        print('Cost of %s: $%d' % (output_serv, (services[user_service])))
        errorInt = 0
    #else:
    except NameError:
        print('Error: Requested service is not recognized')
        
