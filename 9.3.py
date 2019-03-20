## Grant Gasser
## 9.3 File Encryption & Decryption, Caesar's Cipher
## 3/25

#Should be able to encode all ASCII characters (values 0-252), 255-3=252
MAX_ASCII_VAL = 252

#NOTE: ord() function returns ASCII value of character
# chr() function returns corresponding character of int by ASCII (opposite of
# ord())
def create_codex():
    '''
    Inputs: None
    Description: creates dictionary of codes based on Ceasar Cipher shift. So
        each character key has a value that is the character shifted 3 to right
    Returns: dictionary called codes
    '''
    codes = {}

    char = chr(0) #start at ASCII value 0 (NUL)
    ascii = 0

    while ascii <= MAX_ASCII_VAL:
        codes[char] = chr(ascii + 3)
        ascii += 1
        char = chr(ascii)

    return codes


def encrypt(infile, encrypted, codes):
    '''
    Inputs: input file, output file (encrypted input file), dictionary of codes
    Description: encrypts file using 3 char shift (Caesar Cipher), going forward
        3 chars
    Returns:
    '''

    #read each line in file
    for line in infile:
        #read and encrypt each character for each line
        for char in line:
            if char in codes:
                encrypted.write(codes[char])
            else:
                #cant encrypt or decrypt so keep this char the same
                encrypted.write(char)


def decrypt(encrypted, decrypted, codes):
    '''
    Inputs: in file (previously encrypted), out file (decrypted file), dictionary of codes
    Description: decrypts file using 3 char shift (Caesar Cipher), going back 3
        this time
    Returns:
    '''

    for line in encrypted:
        for char in line:
            if char in codes.values():
                for key, val in codes.items():
                    if char == val:
                        decrypted.write(key)

            else:
                decrypted.write(char)



def main():

    codes = create_codex()

    print('This is the code for encrypting files:\n', codes)

    #read in file and encrypt
    infile = open('python.txt', 'r')
    encrypted = open('encrypted.txt', 'w')


    #encrypt infile
    encrypt(infile, encrypted, codes)
    infile.close()
    encrypted.close()

    #re-open 'encrypted' file to read from and decrypt
    encrypted = open('encrypted.txt', 'r')

    #will be decrypted file, should have same contents as 'test.txt' after
    #decrypt() is called
    decrypted = open('decrypted.txt', 'w')

    #decrypt file called 'encrypted'
    decrypt(encrypted, decrypted, codes)

    encrypted.close()
    decrypted.close()

main()
