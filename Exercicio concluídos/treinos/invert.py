def invert_words(word):
    reverse = word[::-1]
    return reverse

def invert_forwords(words):
    invertida = ''
    for letra in words:
        invertida = letra + invertida
    return invertida


print(invert_words('Python'))
print(invert_forwords('Python'))

