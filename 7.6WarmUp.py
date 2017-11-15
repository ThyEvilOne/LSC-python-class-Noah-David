#This work was done by Noah Works and David Blackburn
user_str = ''
while user_str != 'q':
  user_str = str(input('Enter input string:\n'))
  
  if user_str == 'q':
    break
  
  while ',' not in user_str:
    print('Error: No comma in string.\n')
    user_str = str(input('Enter input string:\n'))
  
  new_str = user_str.split(',')
  usr_str = ''
  
  word1 = new_str[0].strip()
  word2 = new_str[1].strip()
  print('First word: %s' % word1)
  print('Second word: %s\n' % word2)
