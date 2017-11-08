codes = {'A':'!', 'B':'@', 'C':'#', 'D':'$', 'E':'%', 'F':'^', 'G':'&', 'H':'*', 'I':'(', 'J':')', 'K':'_', 'L':'-', 'M':'+', 'N':'=', 'O':'1', 'P':'2',
    'Q':'3', 'R':'4', 'S':'5', 'T':'6', 'U':'7', 'V':'8', 'W':'9', 'X':'0', 'Y':'~', 'Z':'`', 'a':'{', 'b':'}', 'c':'[', 'd':']', 'e':'|', 'f':'\\', 'g':':',
    'h':';', 'i':'<', 'j':'>', 'k':',', 'l':'.', 'm':'?', 'n':'/', 'o':'™', 'p':'£', 'q':'¢', 'r':'∞', 's':'§', 't':'¶', 'u':'•', 'v':'ª', 'w':'º', 'x':'≠',
    'y':'«', 'z':'≥', ' ':' ',
}
user_sentence = str(input('Enter in string: '))
encrypted_sentence = []
decrypted_sentence = []
string_encrypted = ''
string_decrypted = ''

def encrypt():
    for i in user_sentence:
        encrypted_sentence.append(codes[i])

    string_encrypted = ''.join(encrypted_sentence)

    return string_encrypted

def decrypt():
    decrypt_codes = dict((y, x) for x, y in codes.items())
    for i in encrypted_sentence:
        decrypted_sentence.append(decrypt_codes[i])

    string_decrypted = ''.join(decrypted_sentence)

    return string_decrypted
        
print(encrypt())
print(decrypt())
