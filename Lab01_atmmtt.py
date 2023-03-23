

clear_text = input (" Enter your secret message: ").lower()
valid_letters = "abcdefghijklmnopqrstuvwxyz "
user_pkey = input ("Enter your key: ").lower()
key  = ""
new_string = ""
cipher_text = []
for char in clear_text:
    if char in valid_letters:
        new_string += char

for char in user_pkey:
    if char in valid_letters:
        if char not in key:
            key += char

for char in valid_letters:
    if char not in key:
        key += char

def encrypt():
    index_values = [valid_letters.index(string) for char in new_string]
    return "".join(key[indexKey] for indexKey in index_values)
print(encrypt())