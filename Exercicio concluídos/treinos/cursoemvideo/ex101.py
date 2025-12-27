

def voto(ano):
    from datetime import date
    hoje = date.today().year
    idadeAtual = hoje - ano
    if idadeAtual < 18:
        # print(f'Com {idadeAtual} anos: NÃO VOTA')
        return f"Com {idadeAtual} anos: NÃO VOTA"
    else:
        if 18 <= idadeAtual < 60:
            return f'Com {idadeAtual} anos: VOTO OBRIGATÓRIO'
        else:
            return f'Com {idadeAtual} anos: VOTO OPCIONAL'



vericado = int(input('Em que ano você nasceu? '))
print(voto(vericado))