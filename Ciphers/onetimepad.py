from numpy.random import randint

cletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
vegenere_table = []
for k in range(27):
    sub_table = []
    for i in range(27):
        sub_table.append(cletters[(cletters.index(cletters[i])+k)%27])
    vegenere_table.append(sub_table)
for i in vegenere_table:
    print(i)

plaintext = "eu amo a minha mae"
key = [cletters[randint(0, 27)] for i in range(len(plaintext))]
print(key)

ciphertext = ''
for i in range(len(plaintext)):
    ciphertext += vegenere_table[cletters.index(plaintext[i])][cletters.index(key[i])]
print(ciphertext)
    
    