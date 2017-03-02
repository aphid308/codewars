import re
def decipher_this(string):
    encrypted_wordlist = string.split(' ')
    decrypted_wordlist = []

    for word in encrypted_wordlist:
        char_code = int((re.findall('\d+', word))[0])
        first_letter = chr(char_code)
        remaining_word = word.lstrip('0123456789')

        if len(remaining_word) < 2:
            decrypted_wordlist.append(first_letter + remaining_word)

        elif len(remaining_word) >= 2:
            decrypted_wordlist.append(first_letter + remaining_word[-1] + remaining_word[1:-1] + remaining_word[0])

    return ' '.join(decrypted_wordlist)


result = decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
print(result)
