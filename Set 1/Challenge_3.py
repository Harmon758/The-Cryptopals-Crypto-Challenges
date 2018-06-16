
import codecs
import string

for character in string.ascii_letters:
    hex_decoded = codecs.decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex").decode()
    decoded = "".join(chr(ord(hex_decoded_character) ^ ord(character)) for hex_decoded_character in hex_decoded)
    if ' ' in decoded:
        print(decoded)
