from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM estado")

    # Obter os resultados
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def inserir(codigo, nome):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para inserir um novo registro
    sql = "INSERT INTO estado (codigo, nome) VALUES (%s, %s)"
    val = (codigo, nome)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()

def atualizar(codigo, novo_nome):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para atualizar o registro
    sql = "UPDATE estado SET nome = %s WHERE codigo = %s"
    val = (novo_nome, codigo)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()

def deletar(codigo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM estado WHERE codigo = %s"
    val = (codigo,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()

# Exemplo de uso
# listar()
# inserir(99, "Estado XPTO")
# atualizar(99, "Estado XYZ")
# deletar(99)


# chama a função conectar
conn = conectar()
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar estados")
  print("2 - Inserir novo estado")
  print("3 - Atualizar um estado")
  print("4 - Deletar um estado")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    # Listar estados
    listar(conn, cursor)
  
  elif opcao == 2:
    # Inserir novo estado
    codigo = int(input("Digite o código do novo estado: "))
    nome = input("Digite o nome do novo estado: ")
    inserir(codigo, nome)

  elif opcao == 3:
    # Atualizar um estado
    codigo = int(input("Digite o código do estado que deseja atualizar: "))
    nome = input("Digite o novo nome do estado: ")
    atualizar(codigo, nome)

  elif opcao == 4:
    # Deletar um estado
    codigo = int(input("Digite o código do estado que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    # Sair do programa
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()