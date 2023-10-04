import numpy as np

cletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
key = np.random.randint(0, 26)
plaintext = "eu durmo de manha"
ciphertext = ""
for i in plaintext:
    ciphertext += cletters[(cletters.index(i)+key)%27]
print(ciphertext)

decrypt = ''
for i in ciphertext:
    decrypt += cletters[(cletters.index(i)-key)%27]
print(decrypt)