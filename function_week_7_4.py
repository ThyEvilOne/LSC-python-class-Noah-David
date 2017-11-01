user_sentence = str(input('Enter sentence: '))

def split():
    user_split = user_sentence.split()
    user_appened = []
    translated_sentence = '' 

    for i in range(len(user_split)):
        user_appened.append(user_split[i][0:] + user_split[i][:1] + 'ay')

    user_appened = [i[1:] for i in user_appened]
    translated_sentence = ' '.join(user_appened)
    
    return translated_sentence.upper()      

print('Translation to pig latin: ', split())
    
