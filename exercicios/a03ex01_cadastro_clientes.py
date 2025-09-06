# Coloque a aplicação dentro de um while para que rode infinitamente, 
# até que o usuário digite 0.
# Nessa aplicação crie um cadastro de clientes = {nome, idade} e
# com as seguintes operações:
# - Inserção de cliente
# - Busca por nome ou id (índice da lista)
# - Remoção 
# - Atualização
#
# Importante: ignore nomes iguais, mas caso exista considere apenas um sem muitos critérios.

clientes = []

def inserir_cliente():
    nome = input("Nome do cliente: ").strip()
    idade = input("Idade do cliente: ").strip()
    # Ignora nomes duplicados
    for cliente in clientes:
        if cliente['nome'].lower() == nome.lower():
            print("Cliente já cadastrado.")
            return
    clientes.append({'nome': nome, 'idade': idade})
    print("Cliente inserido com sucesso.")

def buscar_cliente():
    escolha = input("Buscar por (1) Nome ou (2) Índice? ")
    if escolha == '1':
        nome = input("Nome do cliente: ").strip()
        for idx, cliente in enumerate(clientes):
            if cliente['nome'].lower() == nome.lower():
                print(f"Encontrado: [{idx}] Nome: {cliente['nome']}, Idade: {cliente['idade']}")
                return
        print("Cliente não encontrado.")



    elif escolha == '2':
        try:
            idx = int(input("Índice do cliente: "))
            cliente = clientes[idx]
            print(f"Encontrado: [{idx}] Nome: {cliente['nome']}, Idade: {cliente['idade']}")
        except (ValueError, IndexError):
            print("Índice inválido.")
    else:
        print("Opção inválida.")

def remover_cliente():
    nome = input("Nome do cliente para remover: ").strip()
    for idx, cliente in enumerate(clientes):
        if cliente['nome'].lower() == nome.lower():
            clientes.pop(idx)
            print("Cliente removido.")
            return
    print("Cliente não encontrado.")

def atualizar_cliente():
    nome = input("Nome do cliente para atualizar: ").strip()
    for cliente in clientes:
        if cliente['nome'].lower() == nome.lower():
            nova_idade = input("Nova idade: ").strip()
            cliente['idade'] = nova_idade
            print("Cliente atualizado.")
            return
    print("Cliente não encontrado.")


while True:
    print("\nMenu: ")
    print("1 - Inserir cliente")
    print("2 - Buscar cliente")
    print("3 - Remover cliente")
    print("4 - Atualizar cliente")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_cliente()
    elif opcao == '2':
        buscar_cliente()
    elif opcao == '3':
        remover_cliente()
    elif opcao == '4':
        atualizar_cliente()
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")