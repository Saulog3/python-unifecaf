# RESOLVIDO !!
# Leia todos os caracteres de uma string e retorne todos os 
# caracteres únicos. Por exemplo:
#     aabcc  => b
#     aabbccaafbbbaaacaa  => fc
#     aabbcc => None

def caracteres_unicos(externa):
    resultado = []
    vistos = set()
    n = len(externa)

    for i, ch in enumerate(externa):
        esquerdo = externa[i-1] if i > 0 else None
        direito = externa[i+1] if i < n-1 else None

        if ch != esquerdo and ch != direito and ch not in vistos:
            resultado.append(ch)
            vistos.add(ch)

    return ''.join(resultado) if resultado else None


print(caracteres_unicos("aabcc"))              # esperado: b
print(caracteres_unicos("aabbccaafbbbaaacaa")) # esperado: fc
print(caracteres_unicos("aabbcc"))             # esperado: None
print(caracteres_unicos("abc"))                # esperado: abc
print(caracteres_unicos("aaabaaa"))            # esperado: b
print(caracteres_unicos("xxyzzx"))  