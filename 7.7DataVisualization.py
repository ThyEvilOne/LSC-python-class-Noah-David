#This work was done by Noah Works and David Blackburn
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
  
def print_list():
  print('%33s' % data_name)
  print('%-20s|%23s' % (column1, column2))
  print('--------------------------------------------')
  for x in new_data_list[::2]:
    name = x
    num = new_data_list[new_data_list.index(x) + 1]
    print('%-20s|%23s' % (name,num))

def print_histogram():
  for y in new_data_list[::2]:
    name = y
    num = int(new_data_list[new_data_list.index(y) + 1])
    print('%20s ' % (name), end='')
    print('*' * num)
    
data_name = str(input('Enter a title for the data:'))
print('\nYou entered: %s\n' % data_name)

column1 = str(input('Enter the column 1 header:\n'))
print('You entered: %s\n' % column1)

column2 = str(input('Enter the column 2 header:\n'))
print('You entered: %s\n' % column2)

names1 = []
nums1 = []
data_str = ''
data_list = []
new_data_list = []
while data_str != '-1':
    data_str = str(input('Enter a data point (-1 to stop input):\n'))
    if data_str == '-1':
      break
    
    #if ',' not in data_str:
    if data_str.count(',') < 1:
      print('Error: No comma in string.\n')
      
    elif hasNumbers(data_str) == False :
      print('Error: Comma not followed by an integer.\n')
      
    elif data_str.count(',') > 1:
      print('Error: Too many commas in input.\n')
      
      
    elif data_str != '-1':
      data_list = data_list + data_str.split(',')
      #creates lists of data
      extra_data = data_str.split(',')
      print('Data string: %s' % extra_data[0].strip())
      print('Data integer: %s\n' % extra_data[1].strip())
      names1.append(extra_data[0].strip())
      nums1.append(extra_data[1].strip())
print('')   
for i in data_list:
  new_data_list.append(i.strip())
print_list()
print('')
print_histogram()
