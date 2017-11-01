def vowels():
    user_list = str(input('Enter string: '))

    vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    vowel_count = 0
    
    for i in user_list:
        if i in vowel:
            vowel_count += 1
        else:
            vowel_count = vowel_count
            
    return vowel_count

def consonants():
    user_list = str(input('Enter string: '))

    consonant_lowercase = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonant_uppercase = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    full_consonant_list = consonant_lowercase + consonant_uppercase
    consonant_count = 0
    
    for i in user_list:
        if i in full_consonant_list:
            consonant_count += 1
        else:
            consonant_count = consonant_count

    return consonant_count

print(vowels())
print(consonants())
    
