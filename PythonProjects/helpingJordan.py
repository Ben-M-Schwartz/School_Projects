LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_string = str(input("enter an english phrase in lowercase with no spaces:"))
input_string = input_string.upper()

enc_key = str(input("enter your encryption key:"))
enc_key = enc_key.upper()
enc_string = ""

string_length = len(input_string)

expanded_key = enc_key
expanded_key_length = len(expanded_key)

while expanded_key_length < string_length:
    expanded_key = expanded_key + enc_key
    expanded_key_length = len(expanded_key)

key_position = 0

# run the encryption/decryption code on each symbol in the message string
for letter in input_string:
    if letter in LETTERS:
        
        position = LETTERS.find(letter)
        print(position)

        key_character = expanded_key[key_position]
        print(key_character)
        key_character_position = LETTERS.find(key_character)
        print(key_character_position)
        key_position = key_position + 1

        new_position = (position + key_character_position)
        print(new_position)

        if new_position > 25:
            new_position = new_position-26
            
        new_character = LETTERS[new_position]
        print(new_position)
        enc_string += new_character

print(enc_string)
        
    # Vigenere cipher
    #input: thequickbrownfoxjumpsoverthelazydog; key: potato
    
    # What should come out: IVXQNWRYURHKCTHXCIBDLOOSGHAEEOOMWOZ
    
    #   What does come out: SGDPTHBJAQNVMENWITLORNUDQSGDKZYXCNF
