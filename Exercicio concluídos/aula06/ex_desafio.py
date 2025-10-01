import mysql.connector
from mysql.connector import Error

config = {
    "host": "localhost",   # ou "127.0.0.1"
    "user": "root",
    "password": "amon1010",
    "database": "cadastro_atividade"
}

def connect_db():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        return conn, cursor
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
        raise SystemExit(1)

# Conecta uma vez no início e usa durante a execução
conn, cursor = connect_db()

# Cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT
)
""")
conn.commit()

def inserir():
    nome = input('Nome: ').strip()
    if not nome:
        print("Nome não pode ficar vazio.")
        return
    idade_str = input('Idade: ').strip()
    try:
        idade = int(idade_str) if idade_str != "" else None
    except ValueError:
        print("Idade inválida (use número).")
        return

    # Verifica duplicado por nome (case-insensitive)
    cursor.execute("SELECT id FROM clientes WHERE LOWER(nome) = LOWER(%s)", (nome,))
    if cursor.fetchone():
        print("Duplicado: já existe cliente com esse nome.")
        return

    cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade))
    conn.commit()
    print(f"Cliente inserido com id {cursor.lastrowid}.")

def listar():
    cursor.execute("SELECT id, nome, idade FROM clientes ORDER BY id")
    rows = cursor.fetchall()
    if not rows:
        print("Nenhum cliente cadastrado.")
        return
    for r in rows:
        print(f"{r['id']:>3} | {r['nome']:<30} | {r['idade']} anos")

def buscar():
    while True:
        escolha = input('1 - Buscar por ID\n2 - Buscar por Nome (parcial)\n0 - Voltar\nEscolha: ').strip()
        if escolha == '0':
            return
        if escolha == '1':
            id_str = input('ID: ').strip()
            if not id_str.isdigit():
                print("ID inválido.")
                continue
            cursor.execute("SELECT id, nome, idade FROM clientes WHERE id = %s", (int(id_str),))
            r = cursor.fetchone()
            if r:
                print(f"{r['id']}: {r['nome']} - {r['idade']} anos")
            else:
                print("Não encontrado.")
        elif escolha == '2':
            nome = input('Nome (pode ser parcial): ').strip()
            cursor.execute("SELECT id, nome, idade FROM clientes WHERE nome LIKE %s", (f"%{nome}%",))
            rows = cursor.fetchall()
            if rows:
                for r in rows:
                    print(f"{r['id']}: {r['nome']} - {r['idade']} anos")
            else:
                print("Nenhum resultado.")
        else:
            print("Opção inválida.")

def remover():
    id_str = input('ID do cliente a remover: ').strip()
    if not id_str.isdigit():
        print("ID inválido.")
        return
    cursor.execute("DELETE FROM clientes WHERE id = %s", (int(id_str),))
    if cursor.rowcount > 0:
        conn.commit()
        print("Removido com sucesso.")
    else:
        print("ID não encontrado.")

def atualizar():
    listar()
    print('')
    
    id_str = input('ID do cliente a atualizar: ').strip()
    if not id_str.isdigit():
        print("ID inválido.")
        return
    cursor.execute("SELECT id, nome, idade FROM clientes WHERE id = %s", (int(id_str),))
    r = cursor.fetchone()
    if not r:
        print("ID não encontrado.")
        return

    print(f"Atualizando: {r['id']} - {r['nome']} - {r['idade']}")
    novo_nome = input('Novo nome (enter para manter): ').strip()
    nova_idade = input('Nova idade (enter para manter): ').strip()

    if novo_nome == "":
        novo_nome = r['nome']
    if nova_idade == "":
        nova_idade = r['idade']
    else:
        try:
            nova_idade = int(nova_idade)
        except ValueError:
            print("Idade inválida.")
            return

    cursor.execute("UPDATE clientes SET nome = %s, idade = %s WHERE id = %s", (novo_nome, nova_idade, int(id_str)))
    conn.commit()
    print("Atualizado com sucesso.")

operacoes = {
    '1': inserir,
    '2': buscar,
    '3': remover,
    '4': atualizar,
    '5': listar
}

def menu_loop():
    opcao = None
    while opcao != '0':
        print('\nCADASTRO CLIENTES')
        print('1 - Inserir')
        print('2 - Buscar por nome ou id')
        print('3 - Remover (por ID)')
        print('4 - Atualizar (por ID)')
        print('5 - Listar')
        print('0 - Sair\n')
        opcao = input("Escolha uma opção: ").strip()
        if opcao in operacoes:
            operacoes[opcao]()
        elif opcao == '0':
            print("Encerrando aplicacao...")
        else:
            print("Opção inexistente.")

if __name__ == '__main__':
    try:
        menu_loop()
    finally:
        try:
            cursor.close()
            conn.close()
            print("Conexão encerrada.")
        except Exception:
            pass
