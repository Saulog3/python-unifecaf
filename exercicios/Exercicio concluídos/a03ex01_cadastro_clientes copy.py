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
    removed_name = input('Cliente a remover: ')
    for index, cliente in enumerate(clientes):
        if cliente['nome'].lower() == removed_name.lower():
            clientes.pop(index)
            print('Cliente {} removido com sucesso.'.format(removed_name))


def remove_nome():
    nome_a_remover = input('Nome a remover: ')
    for i, cliente in enumerate(clientes):
        if nome_a_remover == cliente['nome']:
            clientes.pop(i)
            print('Cliente ', nome_a_remover, ' removido')
            
def busca():
    name_to_search = input('Buscar nome: ')
    
    if name_to_search == clientes['nome']:
        




while opcao != '0':
    print("\nMenu:")
    print("1 - Inserir cliente")
    print("2 - Buscar cliente")
    print("3 - Remover cliente")
    print("4 - Atualizar cliente")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastro()
    elif opcao == '2':
        buscar_cliente()
    elif opcao == '3':
        remove_nome()
    elif opcao == '4':
        atualizar_cliente()
    elif opcao == '0':
        print("Saindo...")
        break
    elif opcao == '7':
        print(clientes)
    else:
        print("Opção inválida.")

    