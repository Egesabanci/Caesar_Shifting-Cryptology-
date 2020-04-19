"""
This algorithm called 'Caesar Shifting'.
The encryption method of 'Caesar Shifting' is shifting letters until the key number.
"""

# this function encrypts the message. (Returns => (cypher (string), key_stride (integer)))
def encrypted(key_stride, word):
    stride = (key_stride % len(list(string.ascii_lowercase)))
    word = word.lower().strip()
    alphabet =  list(string.ascii_lowercase) * 100
    cypher = []
    for letter in word:
        for i in alphabet:
            if letter == i:
                pos = alphabet.index(i)
                let = alphabet[pos + stride]
        cypher.append(let)
    cypher = ''.join(cypher)
    return (cypher, stride)

# this function encrypts the message. (Returns => (decode (string), key_stride (integer)))
def decrypted(key_stride, word):
    key_stride = (key_stride % len(list(string.ascii_lowercase)))
    word = word.lower().strip()
    alphabet =  list(string.ascii_lowercase) * 100
    decode = []
    for letter in word:
        for i in alphabet:
            if letter == i:
                pos = alphabet.index(i)
                let = alphabet[pos - key_stride]
        decode.append(let)
    decode = ''.join(decode)
    return (decode, key_stride)
