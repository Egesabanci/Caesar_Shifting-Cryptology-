"""
This algorithm called 'Ceasar Shifting'.
This way of encryption method is shifting letters as key number.
"""

# this function encrypts the message. (Returns => (cypher (string), key_stride (integer)))
def encrypted(key_stride, word):
    stride = (key_stride % 26)
    word = word.lower().strip()
    word = word.replace(' ', '_')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 50
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
    key_stride = (key_stride % 26)
    word = word.lower().strip()
    word = word.replace(' ', '_')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 50
    decode = []
    for letter in word:
        for i in alphabet:
            if letter == i:
                pos = alphabet.index(i)
                let = alphabet[pos - key_stride]
        decode.append(let)
    decode = ''.join(decode)
    return (decode, key_stride)