print('Opening myfile.txt')
my_file = open('myfile.txt', 'r+')

# Open a file for reading and appending
with my_file as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())
    
    product = num1 * num2
    str_prod = str(product)

    # Write back result on own line
    f.write('\n')
    f.write(str_prod)

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')
