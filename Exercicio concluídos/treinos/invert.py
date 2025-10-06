def invert_words(word):
    reverse = word[::-1]
    return reverse

def invert_forwords(words):
    invertida = ''
    for letra in words:
        invertida = letra + invertida
    return invertida

def palindromo(words):
    invertida = ''
    for letra in words:
        invertida = letra + invertida
    if invertida.lower() == words.lower():
        return True
    
def pali2(w):
    if w == invert_words(w):
        return True
    else:
        return False



print(invert_words('Python'))
print(invert_forwords('Python'))
print(palindromo('Arara'))
print(pali2('aara'))

