errorInt = 1
while errorInt == 1:
    try:
        triangle_char = input('Enter a character:\n')
        triangle_height = int(input('Enter triangle height:\n'))
        print('')
        ast_str = ''
        errorInt = 0
    except ValueError:
        print('Error: Height must be an integer.')
    
for i in range(triangle_height):
    ast_str += triangle_char + ' '
    print(ast_str)
