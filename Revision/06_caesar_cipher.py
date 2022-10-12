alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher_encrypt(msg, key):
    encrypted_msg = ''
    key = key % 26
    for char in msg:
        char_index = alphabet.index(char)
        new_index = char_index + key
        if new_index > 25:
            new_index = new_index % 26
        encrypted_msg += alphabet[new_index]

    return encrypted_msg


print(caesar_cipher_encrypt('akash', 2))
