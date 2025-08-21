# RESOLVIDO !!
# Leia todos os caracteres de uma string e retorne todos os 
# caracteres únicos. Por exemplo:
#     aabcc  => b
#     aabbccaafbbbaaacaa  => fc
#     aabbcc => None


def caractaresUnicos(variavel_externa):
    if variavel_externa == None: 
        return None
    
    if len(variavel_externa) == 1:
        return variavel_externa
    
    iguais = 0
    unicos = []
    for i, caracter in enumerate(variavel_externa): 
        if(i + 1 < len(variavel_externa)):
            if(caracter == texto[i + 1]):
                iguais += 1
            else:
                if(iguais == 0):
                    unicos.append(caracter)
                iguais = 0
        else:
            if(iguais == 0):
                    unicos.append(caracter)
    
    if unicos:
        return unicos
    return None

texto = 'aabbccaafbbbaaacaa'
verificado = caractaresUnicos(texto)
print(caractaresUnicos(texto))
print(verificado)
