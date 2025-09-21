# Busque no texto principal o valor digitado pelo usuário, 
# ao final retorne True se o valor for encontrado ou False 
# caso contrário. Deve ser analisado caractere por caractere. 
# Exemplo de entrada e saída:
#     Entrada do usuário: brasil
#     Texto: no brasil existem muitos lugares bonitos
#     Retorno experado: True

def buscar_texto(texto: str, valor: str) -> bool:
    n = len(texto)
    m = len(valor)

    for i in range(n - m + 1):
        if texto[i:i+m] == valor:
            return True
    return False

texto = 'no brasil existem muitos lugares bonitos'
print(buscar_texto(texto, 'brasil'))