alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


def ecrypt_msg(msg, key):
    encrypted_msg_arr = []

    for letter in msg:
        index = alphabet.index(letter)
        modified_index = index + key
        if modified_index > 25:
            modified_index = modified_index - 26
        encrypted_msg_arr.append(alphabet[modified_index])

    encrypted_msg = ''.join(encrypted_msg_arr)
    print(f'Encoded message is {encrypted_msg}')


def decrypt_msg(msg, key):
    decrypt_msg = ''
    for letter in msg:
        index = alphabet.index(letter)
        modified_index = index - key
        decrypt_msg += alphabet[modified_index]
    print(f'Decoded message is{decrypt_msg}')


if direction == 'encode':
    ecrypt_msg(msg=text, key=shift)
elif direction == 'decode':
    decrypt_msg(msg=text, key=shift)
