def initials(name):
	split_string = name.split(' ')
	print('%c. %c. %c.' % split_string[0][0], split_string[1][0], split_string[2][0])

initials(input('Enter full Name: '))
