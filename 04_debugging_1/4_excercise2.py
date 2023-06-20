

def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    # changed 98 to 97 and range to capture entire alphabet
    #list[a,b,c...z]
    #alphabet = [chr(i + 98) for i in range(1, 26)]
    cipher_with_duplicates = list(key) + alphabet
    #list[s,e,c,r,e,t,k,e,y,a,b,c...z]
    #cipher = [s,e,c,r,t,k,y,a,b,d,f,g,h,j,k,l,m...z]

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

def encode(text, key):
    print("text",text)
    #text = theswiftfoxjumpedoverthelazydog
    print("key",key)
    #key = secretkey
    cipher = make_cipher(key)
    #cipher = [s,e,c,r,t,k,y,a,b,d,f,g,h,j,k,l,m...z]

    ciphertext_chars = []
    #ciphertext_chars = ['E', 'M', 'B', 'A', 'X', 'N', 'K', 'E', 'W']
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    #EMBAXNK...
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    #encrypted = EMBAX...
    #key = secretkey
    cipher = make_cipher(key)
    #cipher = ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b'...]

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i)-65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)




# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
