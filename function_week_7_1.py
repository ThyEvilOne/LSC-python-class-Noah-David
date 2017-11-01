def initials(name):
                split_list = name.split(' ')
                print(split_list)
                print('%s. %s. %s.' % (split_list[0][0], split_list[1][0], split_list[2][0]))
	
initials(str(input('Enter full Name: ')))
