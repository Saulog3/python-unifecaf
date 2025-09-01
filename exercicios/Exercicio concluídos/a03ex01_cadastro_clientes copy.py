# Coloque a aplicação dentro de um while para que rode infinitamente, 
# até que o usuário digite 0.
# Nessa aplicação crie um cadastro de clientes = {nome, idade} e
# com as seguintes operações:
# - Inserção de cliente
# - Busca por nome ou id (índice da lista)
# - Remoção 
# - Atualização
# - Listar clientes
# Importante: ignore nomes iguais, mas caso exista considere apenas um sem muitos critérios.

clientes = []
opcao = None
def cadastro():
    nome = input('Nome: ').strip()
    idade = input('Idade: ').strip()
    for cliente in clientes:
        if cliente['nome'].lower() == nome.lower():
            print('Duplicado')
            return

    clientes.append({
        'nome': nome,
        'idade': idade
        })
    
def remover():
    nome = input('Nome a remover: ')
    for i, cliente in enumerate(clientes):
        if nome.lower() == cliente['nome'].lower():
            clientes.pop(i)
            print(f'Cliente {nome} foi removido.')


def listagem():
    for i, cliente in enumerate(clientes):
        print(i, cliente['nome'], cliente['idade'])



def busca():
    
    choose = None
    while choose != '0':
        choose = input('1 - Buscar por ID\n2 - Buscar por Nome\n0 - Voltar\n ')
        if choose == '1':
            identificacao = input('Buscar: ')
            for i, cliente in enumerate(clientes):
                if identificacao == cliente[i]:
                    print(f'''
                        Nº: {i} 
                        Nome: {cliente['nome']} 
                        idade {cliente['idade']}
                        ''')
                
        elif choose == '2':
            nome = input('Buscar: ')
            for i, cliente in enumerate(clientes):
                if nome.lower() == cliente['nome'].lower():
                    print(f'''
                        Nº: {i} 
                        Nome: {cliente['nome']} 
                        idade {cliente['idade']}
                        ''')
        else:
            print('Opção inválida')

def atualiza_cliente():
    nome = input('Nome do cliente a ser atualizado: ')
    for i, cliente in enumerate(clientes):
        if nome.lower() == cliente['nome'].lower():
            novo_nome = input('Novo nome: ')
            nova_idade = input('Nova idade: ')
            clientes[i] = {
                'nome': novo_nome,
                'idade': nova_idade
            }
            print(f'Cliente {nome} atualizado com sucesso.')
            return
    print(f'Cliente {nome} não encontrado.')

operacoes = {
    '1': cadastro,
    '2': busca,
    '3': remover,
    '4': atualiza_cliente,
    '5': listagem,
}

while opcao != '0':
    print('\n')
    print('CADASTRO CLIENTES')
    print('1 - Inserir')
    print('2 - Buscar por nome ou id')
    print('3 - Remover')
    print('4 - Atualizar')
    print('5 - Listar')
    print('0 - Sair')
    print('\n')

    opcao = input("Escolha uma opção: ").strip()

    if opcao in operacoes:
        operacoes[opcao]()
    elif opcao == '0':
        print("Encerrando aplicacao...")
    else:
        print("Opção inexistente")

