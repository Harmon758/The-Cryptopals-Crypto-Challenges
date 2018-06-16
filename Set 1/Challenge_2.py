
def xor(string1, string2):
    # Takes two hex strings of equal length as input and returns a hex string as output
    return f"{int(string1, 16) ^ int(string2, 16):x}"

assert xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"
